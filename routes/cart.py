
"""
Rotas do carrinho de compras
"""
from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_required, current_user
from models import db, Product, Cart, CartItem
from werkzeug.utils import secure_filename
import os
from config import Config

cart_bp = Blueprint('cart', __name__)


def allowed_file(filename):
    """Verifica se o arquivo é permitido"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS


@cart_bp.route('/')
@login_required
def ver_carrinho():
    """Ver carrinho de compras"""
    cart = Cart.query.filter_by(user_id=current_user.id).first()
    
    if not cart:
        cart = Cart(user_id=current_user.id)
        db.session.add(cart)
        db.session.commit()
    
    return render_template('cart/carrinho.html', cart=cart)


@cart_bp.route('/adicionar/<int:product_id>', methods=['POST'])
@login_required
def adicionar(product_id):
    """Adicionar produto ao carrinho"""
    produto = Product.query.get_or_404(product_id)
    quantidade = request.form.get('quantidade', 1, type=int)
    
    # Validar quantidade
    if quantidade < 1:
        flash('Quantidade inválida.', 'danger')
        return redirect(url_for('products.detalhe', id=product_id))
    
    # Pegar ou criar carrinho
    cart = Cart.query.filter_by(user_id=current_user.id).first()
    if not cart:
        cart = Cart(user_id=current_user.id)
        db.session.add(cart)
        db.session.commit()
    
    # Verificar se o produto já está no carrinho
    cart_item = CartItem.query.filter_by(cart_id=cart.id, product_id=product_id).first()
    
    if cart_item:
        # Atualizar quantidade
        cart_item.quantidade += quantidade
    else:
        # Criar novo item
        cart_item = CartItem(
            cart_id=cart.id,
            product_id=product_id,
            quantidade=quantidade
        )
        db.session.add(cart_item)
    
    db.session.commit()
    
    flash(f'{produto.nome} adicionado ao carrinho!', 'success')
    return redirect(url_for('products.detalhe', id=product_id))


@cart_bp.route('/atualizar/<int:item_id>', methods=['POST'])
@login_required
def atualizar(item_id):
    """Atualizar quantidade de item no carrinho"""
    cart_item = CartItem.query.get_or_404(item_id)
    
    # Verificar se o item pertence ao usuário
    if cart_item.cart.user_id != current_user.id:
        flash('Acesso negado.', 'danger')
        return redirect(url_for('cart.ver_carrinho'))
    
    quantidade = request.form.get('quantidade', 1, type=int)
    
    if quantidade < 1:
        flash('Quantidade inválida.', 'danger')
        return redirect(url_for('cart.ver_carrinho'))
    
    cart_item.quantidade = quantidade
    db.session.commit()
    
    flash('Carrinho atualizado!', 'success')
    return redirect(url_for('cart.ver_carrinho'))


@cart_bp.route('/remover/<int:item_id>', methods=['POST'])
@login_required
def remover(item_id):
    """Remover item do carrinho"""
    cart_item = CartItem.query.get_or_404(item_id)
    
    # Verificar se o item pertence ao usuário
    if cart_item.cart.user_id != current_user.id:
        flash('Acesso negado.', 'danger')
        return redirect(url_for('cart.ver_carrinho'))
    
    db.session.delete(cart_item)
    db.session.commit()
    
    flash('Item removido do carrinho.', 'info')
    return redirect(url_for('cart.ver_carrinho'))


@cart_bp.route('/personalizar/<int:item_id>', methods=['POST'])
@login_required
def personalizar(item_id):
    """Adicionar personalização ao item do carrinho"""
    cart_item = CartItem.query.get_or_404(item_id)
    
    # Verificar se o item pertence ao usuário
    if cart_item.cart.user_id != current_user.id:
        flash('Acesso negado.', 'danger')
        return redirect(url_for('cart.ver_carrinho'))
    
    # Pegar texto de personalização
    personalizacao_texto = request.form.get('personalizacao_texto', '')
    cart_item.personalizacao_texto = personalizacao_texto
    
    # Upload de imagem
    if 'personalizacao_imagem' in request.files:
        file = request.files['personalizacao_imagem']
        
        if file and file.filename and allowed_file(file.filename):
            filename = secure_filename(f"custom_{current_user.id}_{item_id}_{file.filename}")
            filepath = os.path.join(Config.UPLOAD_FOLDER, filename)
            
            # Criar diretório se não existir
            os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)
            
            file.save(filepath)
            cart_item.personalizacao_imagem = filename
    
    db.session.commit()
    
    flash('Personalização salva!', 'success')
    return redirect(url_for('cart.ver_carrinho'))


@cart_bp.route('/limpar', methods=['POST'])
@login_required
def limpar():
    """Limpar carrinho"""
    cart = Cart.query.filter_by(user_id=current_user.id).first()
    
    if cart:
        CartItem.query.filter_by(cart_id=cart.id).delete()
        db.session.commit()
    
    flash('Carrinho limpo.', 'info')
    return redirect(url_for('cart.ver_carrinho'))
