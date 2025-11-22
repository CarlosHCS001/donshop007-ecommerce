"""
Rotas de produtos
"""
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from models import db, Product, Review
from config import Config

products_bp = Blueprint('products', __name__)


@products_bp.route('/')
def listar():
    page = request.args.get('page', 1, type=int)
    categoria = request.args.get('categoria', '')
    busca = request.args.get('busca', '')
    ordem = request.args.get('ordem', 'recente')
    
    query = Product.query
    
    # filtra categoria se tiver
    if categoria:
        query = query.filter_by(categoria=categoria)
    
    # busca no nome ou descricao
    if busca:
        query = query.filter(Product.nome.ilike(f'%{busca}%') | Product.descricao.ilike(f'%{busca}%'))
    
    # ordenação
    if ordem == 'menor_preco':
        query = query.order_by(Product.preco.asc())
    elif ordem == 'maior_preco':
        query = query.order_by(Product.preco.desc())
    elif ordem == 'nome':
        query = query.order_by(Product.nome.asc())
    else:
        query = query.order_by(Product.created_at.desc())
    
    produtos = query.paginate(page=page, per_page=Config.PRODUCTS_PER_PAGE, error_out=False)
    
    return render_template('produtos/listar.html', 
                         produtos=produtos,
                         categoria_selecionada=categoria,
                         busca=busca,
                         ordem=ordem)


@products_bp.route('/<int:id>')
def detalhe(id):
    produto = Product.query.get_or_404(id)
    
    # pega as avaliacoes
    reviews = Review.query.filter_by(product_id=id).order_by(Review.created_at.desc()).limit(Config.MAX_REVIEWS_PER_PRODUCT).all()
    
    # verifica se usuario ja avaliou esse produto
    ja_avaliou = False
    if current_user.is_authenticated:
        ja_avaliou = Review.query.filter_by(product_id=id, user_id=current_user.id).first() is not None
    
    # produtos da mesma categoria
    produtos_relacionados = Product.query.filter(
        Product.categoria == produto.categoria,
        Product.id != produto.id
    ).limit(4).all()
    
    return render_template('produtos/detalhe.html',
                         produto=produto,
                         reviews=reviews,
                         ja_avaliou=ja_avaliou,
                         produtos_relacionados=produtos_relacionados)


@products_bp.route('/<int:id>/avaliar', methods=['POST'])
@login_required
def avaliar(id):
    produto = Product.query.get_or_404(id)
    
    # ja avaliou?
    if Review.query.filter_by(product_id=id, user_id=current_user.id).first():
        flash('Você já avaliou este produto.', 'warning')
        return redirect(url_for('products.detalhe', id=id))
    
    # limite de avaliacoes
    if produto.review_count >= Config.MAX_REVIEWS_PER_PRODUCT:
        flash('Este produto já atingiu o limite de avaliações.', 'warning')
        return redirect(url_for('products.detalhe', id=id))
    
    rating = request.form.get('rating', type=int)
    comentario = request.form.get('comentario', '')
    
    if not rating or rating < 1 or rating > 5:
        flash('Avaliação inválida.', 'danger')
        return redirect(url_for('products.detalhe', id=id))
    
    review = Review(
        product_id=id,
        user_id=current_user.id,
        rating=rating,
        comentario=comentario
    )
    
    db.session.add(review)
    db.session.commit()
    
    flash('Avaliação enviada com sucesso!', 'success')
    return redirect(url_for('products.detalhe', id=id))
