import pytest
from app import create_app
from models import db, User, Product


@pytest.fixture
def app_test():
    app = create_app('testing')
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()


def test_init_database_cria_usuarios(app_test):
    """deve criar admin e usuario teste no banco"""
    with app_test.app_context():
        from init_db import init_database
        init_database(app=app_test)

        admin = User.query.filter_by(email="admin@donshop007.com").first()
        cliente = User.query.filter_by(email="cliente@teste.com").first()

        assert admin is not None
        assert admin.is_admin is True
        assert cliente is not None
        assert cliente.is_admin is False


def test_init_database_cria_produtos(app_test):
    """deve criar 9 produtos no banco"""
    with app_test.app_context():
        from init_db import init_database
        init_database(app=app_test)

        total = Product.query.count()
        assert total == 9


def test_init_database_nao_duplica_dados(app_test):
    """se banco ja tem dados, nao deve inserir de novo"""
    with app_test.app_context():
        from init_db import init_database
        init_database(app=app_test)
        init_database(app=app_test)

        total = Product.query.count()
        assert total == 9
