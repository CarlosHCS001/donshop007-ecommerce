"""
Config do DonShop007
"""

import os
from datetime import timedelta

class Config:
    """configurações base"""
    
    # chave secreta (trocar em produção via env)
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-donshop007-change-in-production'
    
    # DB: usar DATABASE_URL ou fallback sqlite local
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///donshop007.db'
    # correção para providers que retornam 'postgres://'
    if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith('postgres://'):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace('postgres://', 'postgresql://', 1)
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False  # True para log de queries
    
    # uploads
    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'uploads')
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5 MB
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    
    # sessão
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)
    SESSION_COOKIE_SECURE = False  # True em produção (HTTPS)
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    
    # paginação
    PRODUCTS_PER_PAGE = 9
    ORDERS_PER_PAGE = 10
    
    # frete (simulado por região)
    FRETE_SUDESTE = 15.00
    FRETE_SUL = 20.00
    FRETE_NORDESTE = 25.00
    FRETE_NORTE = 30.00
    FRETE_CENTRO_OESTE = 22.00
    
    # avaliações
    MAX_REVIEWS_PER_PRODUCT = 10

class DevelopmentConfig(Config):
    """config dev"""
    DEBUG = True
    SQLALCHEMY_ECHO = False

class ProductionConfig(Config):
    """config produção"""
    DEBUG = False
    SESSION_COOKIE_SECURE = True

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
