import pytest
from unittest.mock import patch, MagicMock
from routes.orders import calcular_frete
from models import db, User, Cart, Product, Order


class TestOrders:

    def _criar_usuario_e_logar(self, client, app):
        with app.app_context():
            user = User(nome="Carlos", email="orders@email.com")
            user.set_password("senha123")
            db.session.add(user)
            db.session.commit()

        client.post('/auth/login', data={
            'email': 'orders@email.com',
            'senha': 'senha123'
        }, follow_redirects=True)

    def test_checkout_sem_login_redireciona(self, client):
        response = client.get('/pedidos/checkout')
        assert response.status_code == 302

    def test_meus_pedidos_sem_login_redireciona(self, client):
        response = client.get('/pedidos/meus-pedidos')
        assert response.status_code == 302

    def test_checkout_com_carrinho_vazio(self, client, app):
        self._criar_usuario_e_logar(client, app)
        response = client.get('/pedidos/checkout', follow_redirects=True)
        assert response.status_code == 200

    def test_meus_pedidos_com_login(self, client, app):
        self._criar_usuario_e_logar(client, app)
        response = client.get('/pedidos/meus-pedidos', follow_redirects=True)
        assert response.status_code == 200

    def test_calcular_frete_sudeste(self):
        """testa frete para SP sem chamar API real"""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'uf': 'SP',
            'logradouro': 'Avenida Paulista',
            'bairro': 'Bela Vista',
            'localidade': 'São Paulo'
        }

        with patch('routes.orders.requests.get', return_value=mock_response):
            frete, dados = calcular_frete('00000000')

        assert frete == 15.00
        assert dados['uf'] == 'SP'
