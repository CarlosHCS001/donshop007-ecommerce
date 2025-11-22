"""
Rotas de pedidos
"""
from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_required, current_user
from models import db, Cart, CartItem, Order, OrderItem
import requests
from config import Config

orders_bp = Blueprint('orders', __name__)


def calcular_frete(cep):
    # consulta o viacep e retorna o valor do frete por região
    try:
        response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        
        if response.status_code != 200:
            return None, None
        
        data = response.json()
        
        if 'erro' in data:
            return None, None
        
        estado = data.get('uf', '')
        
        # define frete por região
        sudeste = ['SP', 'RJ', 'MG', 'ES']
        sul = ['PR', 'SC', 'RS']
        nordeste = ['BA', 'SE', 'AL', 'PE', 'PB', 'RN', 'CE', 'PI', 'MA']
        norte = ['AM', 'RR', 'AP', 'PA', 'TO', 'RO', 'AC']
        centro_oeste = ['MT', 'MS', 'GO', 'DF']
        
        if estado in sudeste:
            frete = Config.FRETE_SUDESTE
        elif estado in sul:
            frete = Config.FRETE_SUL
        elif estado in nordeste:
            frete = Config.FRETE_NORDESTE
        elif estado in norte:
            frete = Config.FRETE_NORTE
        elif estado in centro_oeste:
            frete = Config.FRETE_CENTRO_OESTE
        else:
            frete = 20.00
        
        return frete, data
    
    except Exception:
        return None, None


@orders_bp.route('/checkout', methods=['GET', 'POST'])
@login_required
def checkout():
    cart = Cart.query.filter_by(user_id=current_user.id).first()
    
    if not cart or cart.item_count == 0:
        flash('Seu carrinho está vazio.', 'warning')
        return redirect(url_for('cart.ver_carrinho'))
    
    if request.method == 'POST':
        # dados do form
        nome_destinatario = request.form.get('nome_destinatario')
        cep = request.form.get('cep', '').replace('-', '').replace('.', '')
        endereco = request.form.get('endereco')
        numero = request.form.get('numero')
        complemento = request.form.get('complemento', '')
        bairro = request.form.get('bairro')
        cidade = request.form.get('cidade')
        estado = request.form.get('estado')
        
        if not all([nome_destinatario, cep, endereco, numero, bairro, cidade, estado]):
            flash('Preencha todos os campos obrigatórios.', 'danger')
            return render_template('orders/checkout.html', cart=cart)
        
        frete, dados_cep = calcular_frete(cep)
        
        if frete is None:
            flash('CEP inválido. Por favor, verifique.', 'danger')
            return render_template('orders/checkout.html', cart=cart)
        
        # cria o pedido
        order = Order(
            user_id=current_user.id,
            total=cart.total,
            frete=frete,
            status='pendente',
            nome_destinatario=nome_destinatario,
            cep=cep,
            endereco=endereco,
            numero=numero,
            complemento=complemento,
            bairro=bairro,
            cidade=cidade,
            estado=estado
        )
        
        db.session.add(order)
        db.session.flush()
        
        # adiciona os itens do carrinho no pedido
        for cart_item in cart.items:
            order_item = OrderItem(
                order_id=order.id,
                product_id=cart_item.product_id,
                quantidade=cart_item.quantidade,
                preco_unitario=cart_item.product.preco,
                personalizacao_texto=cart_item.personalizacao_texto,
                personalizacao_imagem=cart_item.personalizacao_imagem
            )
            db.session.add(order_item)
        
        # limpa o carrinho
        CartItem.query.filter_by(cart_id=cart.id).delete()
        db.session.commit()
        
        return redirect(url_for('orders.pagamento', order_id=order.id))
    
    return render_template('orders/checkout.html', cart=cart)


@orders_bp.route('/consultar-cep/<cep>')
@login_required
def consultar_cep(cep):
    cep = cep.replace('-', '').replace('.', '')
    frete, dados = calcular_frete(cep)
    
    if frete is None:
        return jsonify({'error': 'CEP inválido'}), 400
    
    return jsonify({
        'frete': frete,
        'endereco': dados.get('logradouro', ''),
        'bairro': dados.get('bairro', ''),
        'cidade': dados.get('localidade', ''),
        'estado': dados.get('uf', '')
    })


@orders_bp.route('/pagamento/<int:order_id>', methods=['GET', 'POST'])
@login_required
def pagamento(order_id):
    order = Order.query.get_or_404(order_id)
    
    # verifica se é do usuario
    if order.user_id != current_user.id:
        flash('Acesso negado.', 'danger')
        return redirect(url_for('main.index'))
    
    if request.method == 'POST':
        # desconta do estoque
        for item in order.items:
            item.product.estoque -= item.quantidade
        
        order.status = 'pago'
        db.session.commit()
        
        flash('Pagamento realizado com sucesso! Pedido confirmado.', 'success')
        return redirect(url_for('orders.confirmacao', order_id=order.id))
    
    return render_template('orders/pagamento.html', order=order)


@orders_bp.route('/confirmacao/<int:order_id>')
@login_required
def confirmacao(order_id):
    order = Order.query.get_or_404(order_id)
    
    if order.user_id != current_user.id:
        flash('Acesso negado.', 'danger')
        return redirect(url_for('main.index'))
    
    return render_template('orders/confirmacao.html', order=order)


@orders_bp.route('/meus-pedidos')
@login_required
def meus_pedidos():
    page = request.args.get('page', 1, type=int)
    
    pedidos = Order.query.filter_by(user_id=current_user.id).order_by(
        Order.created_at.desc()
    ).paginate(page=page, per_page=Config.ORDERS_PER_PAGE, error_out=False)
    
    return render_template('orders/meus_pedidos.html', orders=pedidos)


@orders_bp.route('/detalhes/<int:order_id>')
@login_required
def detalhes(order_id):
    order = Order.query.get_or_404(order_id)
    
    if order.user_id != current_user.id:
        flash('Acesso negado.', 'danger')
        return redirect(url_for('main.index'))
    
    return render_template('orders/detalhes.html', order=order)
