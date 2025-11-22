
"""
Aplicação principal do DonShop007
E-commerce de produtos personalizados
"""
import os
from flask import Flask, render_template
from flask_login import LoginManager
from flask_migrate import Migrate
from config import config
from models import db, User

# Importar blueprints
from routes.main import main_bp
from routes.auth import auth_bp
from routes.products import products_bp
from routes.cart import cart_bp
from routes.orders import orders_bp
from routes.admin import admin_bp

def create_app(config_name='default'):
    """Factory function para criar a aplicação Flask"""
    
    app = Flask(__name__)
    
    # Carregar configurações
    app.config.from_object(config[config_name])
    
    # Inicializar extensões
    db.init_app(app)
    migrate = Migrate(app, db)
    
    # Configurar Flask-Login
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Por favor, faça login para acessar esta página.'
    login_manager.login_message_category = 'info'
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    # Registrar blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(products_bp, url_prefix='/produtos')
    app.register_blueprint(cart_bp, url_prefix='/carrinho')
    app.register_blueprint(orders_bp, url_prefix='/pedidos')
    app.register_blueprint(admin_bp, url_prefix='/admin')
    
    # Context processor para templates
    @app.context_processor
    def inject_cart_count():
        """Injeta a contagem de itens do carrinho em todos os templates"""
        from flask_login import current_user
        from models import Cart
        
        cart_count = 0
        if current_user.is_authenticated:
            cart = Cart.query.filter_by(user_id=current_user.id).first()
            if cart:
                cart_count = cart.item_count
        
        return dict(cart_count=cart_count)
    
    # Handler de erro 404
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html'), 404
    
    # Handler de erro 500
    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('errors/500.html'), 500
    
    # Criar tabelas do banco de dados
    with app.app_context():
        db.create_all()
    
    return app


# Criar aplicação
app = create_app(os.getenv('FLASK_ENV', 'development'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
