"""
Rotas do carrinho
"""
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from models import db, Product, Cart, CartItem
from werkzeug.utils import secure_filename
import os
from config import Config

cart_bp = Blueprint('cart', __name__)


def allowed_file(filename):
    # checa se a extensão é permitida
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS


@cart_bp.route('/')
@login_required
def ver_carrinho():
    cart = Cart.query.filter_by(user_id=current_user.id).first()
    
    # se não tem carrinho ainda, cria um
    if not cart:
        cart = Cart(user_id=current_user.id)
        db.session.add(cart)
        db.session.commit()
    
    return render_template('cart/carrinho.html', cart=cart)


@cart_bp.route('/adicionar/<int:product_id>', methods=['POST'])
@login_required
def adicionar(product_id):
    produto = Product.query.get_or_404(product_id)
    quantidade = request.form.get('quantidade', 1, type=int)
    
    if quantidade < 1:
        flash('Quantidade inválida.', 'danger')
        return redirect(url_for('products.detalhe', id=product_id))
    
    # pega carrinho ou cria se não existir
    cart = Cart.query.filter_by(user_id=current_user.id).first()
    if not cart:
        cart = Cart(user_id=current_user.id)
        db.session.add(cart)
        db.session.commit()
    
    # verifica se produto já tá no carrinho
    cart_item = CartItem.query.filter_by(cart_id=cart.id, product_id=product_id).first()
    
    if cart_item:
        cart_item.quantidade += quantidade
    else:
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
    cart_item = CartItem.query.get_or_404(item_id)
    
    # segurança - verifica se é do usuario
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
    cart_item = CartItem.query.get_or_404(item_id)
    
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
    cart_item = CartItem.query.get_or_404(item_id)
    
    if cart_item.cart.user_id != current_user.id:
        flash('Acesso negado.', 'danger')
        return redirect(url_for('cart.ver_carrinho'))
    
    # texto da personalizacao
    personalizacao_texto = request.form.get('personalizacao_texto', '')
    cart_item.personalizacao_texto = personalizacao_texto
    
    # upload da imagem se tiver
    if 'personalizacao_imagem' in request.files:
        file = request.files['personalizacao_imagem']
        
        if file and file.filename and allowed_file(file.filename):
            filename = secure_filename(f"custom_{current_user.id}_{item_id}_{file.filename}")
            filepath = os.path.join(Config.UPLOAD_FOLDER, filename)
            
            os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)
            
            file.save(filepath)
            cart_item.personalizacao_imagem = filename
    
    db.session.commit()
    
    flash('Personalização salva!', 'success')
    return redirect(url_for('cart.ver_carrinho'))


@cart_bp.route('/limpar', methods=['POST'])
@login_required
def limpar():
    cart = Cart.query.filter_by(user_id=current_user.id).first()
    
    if cart:
        CartItem.query.filter_by(cart_id=cart.id).delete()
        db.session.commit()
    
    flash('Carrinho limpo.', 'info')
    return redirect(url_for('cart.ver_carrinho'))
