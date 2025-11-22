
"""
Rotas principais do site (home, sobre, etc)
"""
from flask import Blueprint, render_template
from models import Product

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    """Página inicial"""
    # Pegar produtos em destaque (primeiros 6)
    produtos_destaque = Product.query.limit(6).all()
    
    return render_template('index.html', produtos=produtos_destaque)


@main_bp.route('/sobre')
def sobre():
    """Página sobre nós"""
    return render_template('sobre.html')


@main_bp.route('/contato')
def contato():
    """Página de contato"""
    return render_template('contato.html')
