
"""
Configurações do projeto DonShop007
"""
import os
from datetime import timedelta

class Config:
    """Configuração base do aplicativo"""
    
    # Chave secreta para sessões e CSRF
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-donshop007-change-in-production'
    
    # Configurações do banco de dados
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///donshop007.db'
    
    # Correção para Heroku/Render (postgres:// -> postgresql://)
    if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith('postgres://'):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace('postgres://', 'postgresql://', 1)
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False  # True para debug de queries SQL
    
    # Configurações de upload
    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'uploads')
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5MB max
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    
    # Configurações de sessão
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)
    SESSION_COOKIE_SECURE = False  # True em produção com HTTPS
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    
    # Configurações de paginação
    PRODUCTS_PER_PAGE = 9
    ORDERS_PER_PAGE = 10
    
    # Configurações de frete (simulado)
    FRETE_SUDESTE = 15.00
    FRETE_SUL = 20.00
    FRETE_NORDESTE = 25.00
    FRETE_NORTE = 30.00
    FRETE_CENTRO_OESTE = 22.00
    
    # Limite de avaliações por produto
    MAX_REVIEWS_PER_PRODUCT = 10

class DevelopmentConfig(Config):
    """Configurações para desenvolvimento"""
    DEBUG = True
    SQLALCHEMY_ECHO = False

class ProductionConfig(Config):
    """Configurações para produção"""
    DEBUG = False
    SESSION_COOKIE_SECURE = True

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
