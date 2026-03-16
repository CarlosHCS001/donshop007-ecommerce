import pytest
from models import User, Product

@pytest.fixture
def usuario(db):
    user = User(nome="Carlos",  email="carlos@teste.com")
    user.set_password("senha123")
    db.session.add(user)
    db.session.commit()
    return user

@pytest.fixture
def produto(db):
    product = Product(
        nome="Caneca Personalizada",
        descricao="Caneca branca 300ml",
        preco=49.90,
        categoria="caneca",
        imagem_url="/static/images/caneca.jpg"
    )
    db.session.add(product)
    db.session.commit()
    return product

def test_usuario_is_not_admin(usuario):
    assert usuario.is_admin == False

def test_produto_average_rating_sem_reviews(produto):
    assert produto.average_rating == 0

def test_user_creation(db):
    """"testa criação de usuàrio"""
    user = User(nome="Carlos", email="carlos@teste.com")
    user.set_password("senha123")
    db.session.add(user)
    db.session.commit()

    saved = User.query.filter_by(email="carlos@teste.com").first()
    assert saved is not None
    assert saved.nome == "Carlos"
    assert saved.is_admin == False

def test_user_password(db):
    """Testa verificação de senha"""
    user = User(nome="Carlos", email="carlos@teste.com")
    user.set_password("senha123")
    db.session.add(user)
    db.session.commit()

    assert user.check_password("senha123") == True
    assert user.check_password("senhaerrada") == False

def test_product_creation(db):
    """testa criação de produto"""
    product = Product(
        nome="Caneca Personalizada",
        descricao="Caneca branca 300ml",
        preco=49.90,
        categoria="Caneca",
        imagem_url = "/static/images/caneca.jpg"
    )
    db.session.add(product)
    db.session.commit()

    saved = Product.query.filter_by(nome="Caneca Personalizada").first()
    assert saved is not None
    assert saved.preco == 49.90
    assert saved.estoque == 100
