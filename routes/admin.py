"""
Rotas do painel administrativo
"""
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from functools import wraps
from models import db, Product, Order, User, Review
from werkzeug.utils import secure_filename
import os
from config import Config

admin_bp = Blueprint('admin', __name__)


def admin_required(f):
    """Decorator para rotas que exigem admin"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            flash('Acesso negado. Você precisa ser administrador.', 'danger')
            return redirect(url_for('main.index'))
        return f(*args, **kwargs)
    return decorated_function


@admin_bp.route('/')
@login_required
@admin_required
def dashboard():
    """Dashboard administrativo"""
    # Estatísticas
    total_produtos = Product.query.count()
    total_usuarios = User.query.count()
    total_pedidos = Order.query.count()
    
    # Pedidos recentes
    pedidos_recentes = Order.query.order_by(Order.created_at.desc()).limit(5).all()
    
    # Produtos com baixo estoque
    produtos_estoque_baixo = Product.query.filter(Product.estoque < 10).all()
    
    return render_template('admin/dashboard.html',
                         total_produtos=total_produtos,
                         total_usuarios=total_usuarios,
                         total_pedidos=total_pedidos,
                         pedidos_recentes=pedidos_recentes,
                         produtos_estoque_baixo=produtos_estoque_baixo)


# ===== GERENCIAMENTO DE PRODUTOS =====

@admin_bp.route('/produtos')
@login_required
@admin_required
def listar_produtos():
    """Lista todos os produtos"""
    page = request.args.get('page', 1, type=int)
    produtos = Product.query.order_by(Product.created_at.desc()).paginate(
        page=page, per_page=20, error_out=False
    )
    
    return render_template('admin/produtos_listar.html', produtos=produtos)


@admin_bp.route('/produtos/novo', methods=['GET', 'POST'])
@login_required
@admin_required
def novo_produto():
    """Criar novo produto"""
    if request.method == 'POST':
        nome = request.form.get('nome')
        descricao = request.form.get('descricao')
        preco = request.form.get('preco', type=float)
        categoria = request.form.get('categoria')
        imagem_url = request.form.get('imagem_url')
        estoque = request.form.get('estoque', 100, type=int)
        
        # Validações
        if not all([nome, descricao, preco, categoria, imagem_url]):
            flash('Preencha todos os campos obrigatórios.', 'danger')
            return render_template('admin/produto_form.html', produto=None)
        
        produto = Product(
            nome=nome,
            descricao=descricao,
            preco=preco,
            categoria=categoria,
            imagem_url=imagem_url,
            estoque=estoque
        )
        
        db.session.add(produto)
        db.session.commit()
        
        flash('Produto criado com sucesso!', 'success')
        return redirect(url_for('admin.listar_produtos'))
    
    return render_template('admin/produto_form.html', produto=None)


@admin_bp.route('/produtos/editar/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def editar_produto(id):
    """Editar produto"""
    produto = Product.query.get_or_404(id)
    
    if request.method == 'POST':
        produto.nome = request.form.get('nome')
        produto.descricao = request.form.get('descricao')
        produto.preco = request.form.get('preco', type=float)
        produto.categoria = request.form.get('categoria')
        produto.imagem_url = request.form.get('imagem_url')
        produto.estoque = request.form.get('estoque', type=int)
        
        db.session.commit()
        
        flash('Produto atualizado com sucesso!', 'success')
        return redirect(url_for('admin.listar_produtos'))
    
    return render_template('admin/produto_form.html', produto=produto)


@admin_bp.route('/produtos/excluir/<int:id>', methods=['POST'])
@login_required
@admin_required
def excluir_produto(id):
    """Excluir produto"""
    produto = Product.query.get_or_404(id)
    
    db.session.delete(produto)
    db.session.commit()
    
    flash('Produto excluído com sucesso!', 'success')
    return redirect(url_for('admin.listar_produtos'))


# ===== GERENCIAMENTO DE PEDIDOS =====

@admin_bp.route('/pedidos')
@login_required
@admin_required
def listar_pedidos():
    """Lista todos os pedidos"""
    page = request.args.get('page', 1, type=int)
    status = request.args.get('status', '')
    
    query = Order.query
    
    if status:
        query = query.filter_by(status=status)
    
    pedidos = query.order_by(Order.created_at.desc()).paginate(
        page=page, per_page=20, error_out=False
    )
    
    return render_template('admin/pedidos_listar.html', pedidos=pedidos, status_filtro=status)


@admin_bp.route('/pedidos/<int:id>')
@login_required
@admin_required
def ver_pedido(id):
    """Ver detalhes do pedido"""
    pedido = Order.query.get_or_404(id)
    
    return render_template('admin/pedido_detalhes.html', pedido=pedido)


@admin_bp.route('/pedidos/<int:id>/atualizar-status', methods=['POST'])
@login_required
@admin_required
def atualizar_status_pedido(id):
    """Atualizar status do pedido"""
    pedido = Order.query.get_or_404(id)
    
    novo_status = request.form.get('status')
    
    if novo_status in ['pendente', 'pago', 'enviado', 'entregue', 'cancelado']:
        pedido.status = novo_status
        db.session.commit()
        
        flash('Status atualizado com sucesso!', 'success')
    else:
        flash('Status inválido.', 'danger')
    
    return redirect(url_for('admin.ver_pedido', id=id))


# ===== GERENCIAMENTO DE USUÁRIOS =====

@admin_bp.route('/usuarios')
@login_required
@admin_required
def listar_usuarios():
    """Lista todos os usuários"""
    page = request.args.get('page', 1, type=int)
    usuarios = User.query.order_by(User.created_at.desc()).paginate(
        page=page, per_page=20, error_out=False
    )
    
    return render_template('admin/usuarios_listar.html', usuarios=usuarios)


@admin_bp.route('/usuarios/<int:id>')
@login_required
@admin_required
def ver_usuario(id):
    """Ver detalhes do usuário"""
    usuario = User.query.get_or_404(id)
    
    return render_template('admin/usuario_detalhes.html', usuario=usuario)


@admin_bp.route('/usuarios/<int:id>/toggle-admin', methods=['POST'])
@login_required
@admin_required
def toggle_admin(id):
    """Alternar status de admin do usuário"""
    usuario = User.query.get_or_404(id)
    
    # Não permitir remover admin de si mesmo
    if usuario.id == current_user.id:
        flash('Você não pode remover seu próprio status de admin.', 'warning')
        return redirect(url_for('admin.ver_usuario', id=id))
    
    usuario.is_admin = not usuario.is_admin
    db.session.commit()
    
    status = 'administrador' if usuario.is_admin else 'usuário comum'
    flash(f'Usuário agora é {status}.', 'success')
    
    return redirect(url_for('admin.ver_usuario', id=id))


# ===== GERENCIAMENTO DE AVALIAÇÕES =====

@admin_bp.route('/avaliacoes')
@login_required
@admin_required
def listar_avaliacoes():
    """Lista todas as avaliações"""
    page = request.args.get('page', 1, type=int)
    avaliacoes = Review.query.order_by(Review.created_at.desc()).paginate(
        page=page, per_page=20, error_out=False
    )
    
    return render_template('admin/avaliacoes_listar.html', avaliacoes=avaliacoes)


@admin_bp.route('/avaliacoes/excluir/<int:id>', methods=['POST'])
@login_required
@admin_required
def excluir_avaliacao(id):
    """Excluir avaliação"""
    avaliacao = Review.query.get_or_404(id)
    
    db.session.delete(avaliacao)
    db.session.commit()
    
    flash('Avaliação excluída com sucesso!', 'success')
    return redirect(url_for('admin.listar_avaliacoes'))
