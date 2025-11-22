"""
Modelos do DonShop007
"""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(UserMixin, db.Model):
    """usuário"""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    senha_hash = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # relacionamentos
    reviews = db.relationship('Review', backref='user', lazy='dynamic', cascade='all, delete-orphan')
    orders = db.relationship('Order', backref='user', lazy='dynamic', cascade='all, delete-orphan')
    cart = db.relationship('Cart', backref='user', uselist=False, cascade='all, delete-orphan')

    def set_password(self, password):
        """define senha (hash)"""
        self.senha_hash = generate_password_hash(password)

    def check_password(self, password):
        """verifica senha"""
        return check_password_hash(self.senha_hash, password)

    def __repr__(self):
        return f'<User {self.email}>'

class Product(db.Model):
    """produto"""
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    preco = db.Column(db.Float, nullable=False)
    categoria = db.Column(db.String(50), nullable=False, index=True)  # caneca, copo, camisa
    imagem_url = db.Column(db.String(200), nullable=False)
    estoque = db.Column(db.Integer, default=100)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # relacionamentos
    reviews = db.relationship('Review', backref='product', lazy='dynamic', cascade='all, delete-orphan')
    order_items = db.relationship('OrderItem', backref='product', lazy='dynamic')
    cart_items = db.relationship('CartItem', backref='product', lazy='dynamic')

    @property
    def average_rating(self):
        """média de avaliações"""
        reviews = self.reviews.all()
        if not reviews:
            return 0
        return sum(r.rating for r in reviews) / len(reviews)

    @property
    def review_count(self):
        """número de avaliações"""
        return self.reviews.count()

    def __repr__(self):
        return f'<Product {self.nome}>'

class Review(db.Model):
    """avaliação de produto"""
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)  # 1-5 estrelas
    comentario = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # índice composto: 1 avaliação por usuário/produto
    __table_args__ = (
        db.UniqueConstraint('product_id', 'user_id', name='unique_review_per_user_product'),
    )

    def __repr__(self):
        return f'<Review {self.id} - Product {self.product_id}>'

class Order(db.Model):
    """pedido"""
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    total = db.Column(db.Float, nullable=False)
    frete = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='pendente')  # pendente, pago, enviado, entregue, cancelado

    # dados de entrega
    nome_destinatario = db.Column(db.String(100))
    cep = db.Column(db.String(10))
    endereco = db.Column(db.String(200))
    numero = db.Column(db.String(20))
    complemento = db.Column(db.String(100))
    bairro = db.Column(db.String(100))
    cidade = db.Column(db.String(100))
    estado = db.Column(db.String(2))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # relacionamentos
    items = db.relationship('OrderItem', backref='order', lazy='dynamic', cascade='all, delete-orphan')

    @property
    def total_com_frete(self):
        """total do pedido + frete"""
        return self.total + self.frete

    def __repr__(self):
        return f'<Order {self.id}>'

class OrderItem(db.Model):
    """item do pedido"""
    __tablename__ = 'order_items'

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    preco_unitario = db.Column(db.Float, nullable=False)
    personalizacao_texto = db.Column(db.Text)
    personalizacao_imagem = db.Column(db.String(200))  # nome do arquivo

    @property
    def subtotal(self):
        """subtotal do item"""
        return self.quantidade * self.preco_unitario

    def __repr__(self):
        return f'<OrderItem {self.id}>'

class Cart(db.Model):
    """carrinho de compras"""
    __tablename__ = 'carts'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # relacionamentos
    items = db.relationship('CartItem', backref='cart', lazy='dynamic', cascade='all, delete-orphan')

    @property
    def total(self):
        """total do carrinho"""
        return sum(item.subtotal for item in self.items)

    @property
    def item_count(self):
        """número total de itens"""
        return sum(item.quantidade for item in self.items)

    def __repr__(self):
        return f'<Cart {self.id}>'

class CartItem(db.Model):
    """item do carrinho"""
    __tablename__ = 'cart_items'

    id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('carts.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False, default=1)
    personalizacao_texto = db.Column(db.Text)
    personalizacao_imagem = db.Column(db.String(200))

    # índice composto: 1 item por produto no carrinho
    __table_args__ = (
        db.UniqueConstraint('cart_id', 'product_id', name='unique_product_per_cart'),
    )

    @property
    def subtotal(self):
        """subtotal do item"""
        return self.quantidade * self.product.preco

    def __repr__(self):
        return f'<CartItem {self.id}>'
