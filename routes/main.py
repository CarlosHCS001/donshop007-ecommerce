"""
Rotas principais
"""
from flask import Blueprint, render_template
from models import Product

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    # pega os 6 primeiros produtos pra mostrar na home
    produtos_destaque = Product.query.limit(6).all()
    return render_template('index.html', produtos=produtos_destaque)


@main_bp.route('/sobre')
def sobre():
    return render_template('sobre.html')


@main_bp.route('/contato')
def contato():
    return render_template('contato.html')
