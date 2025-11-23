"""
DonShop007 - App principal
E-commerce de produtos personalizados
"""

import os
from flask import Flask, render_template
from flask_login import LoginManager
from flask_migrate import Migrate
from config import config
from models import db, User

# blueprints
from routes.main import main_bp
from routes.auth import auth_bp
from routes.products import products_bp
from routes.cart import cart_bp
from routes.orders import orders_bp
from routes.admin import admin_bp

def create_app(config_name='default'):
    """cria app Flask com configurações e extensões"""
    
    app = Flask(__name__)
    
    # carrega config
    app.config.from_object(config[config_name])
    
    # inicia extensões
    db.init_app(app)
    migrate = Migrate(app, db)
    
    # configura login
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Faça login para continuar.'
    login_manager.login_message_category = 'info'
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    # registra blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(products_bp, url_prefix='/produtos')
    app.register_blueprint(cart_bp, url_prefix='/carrinho')
    app.register_blueprint(orders_bp, url_prefix='/pedidos')
    app.register_blueprint(admin_bp, url_prefix='/admin')
    
    # injeta contagem do carrinho nos templates
    @app.context_processor
    def inject_cart_count():
        from flask_login import current_user
        from models import Cart
        
        cart_count = 0
        if current_user.is_authenticated:
            cart = Cart.query.filter_by(user_id=current_user.id).first()
            if cart:
                cart_count = cart.item_count
        
        return dict(cart_count=cart_count)
    
    # erros 404 e 500
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html'), 404
    
    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('errors/500.html'), 500
    
    # cria tabelas
    with app.app_context():
        db.create_all()
    
    return app

# inicia app
app = create_app(os.getenv('FLASK_ENV', 'development'))

# Rota temporária para inicializar banco de dados (REMOVER DEPOIS)
@app.route('/iniciar-banco-2024')
def iniciar_banco():
    from init_db import init_database
    try:
        init_database()
        return '''
        <html>
        <head>
            <title>Banco Inicializado</title>
            <style>
                body { font-family: Arial; padding: 50px; text-align: center; }
                h1 { color: green; }
                .info { background: #f0f0f0; padding: 20px; margin: 20px auto; max-width: 500px; border-radius: 10px; }
                .warning { color: red; font-weight: bold; }
                a { display: inline-block; margin-top: 20px; padding: 10px 20px; background: #007bff; color: white; text-decoration: none; border-radius: 5px; }
            </style>
        </head>
        <body>
            <h1>✅ Banco de Dados Criado com Sucesso!</h1>
            <div class="info">
                <p><strong>Usuário Admin:</strong> admin@donshop007.com</p>
                <p><strong>Senha:</strong> admin123</p>
            </div>
            <p class="warning">⚠️ IMPORTANTE: Remova esta rota do código por segurança!</p>
            <a href="/auth/login">Fazer Login Agora</a>
        </body>
        </html>
        '''
    except Exception as e:
        return f'<h1 style="color: red;">❌ Erro ao criar banco:</h1><p>{str(e)}</p>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
