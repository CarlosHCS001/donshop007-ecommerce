import pytest
from models import db, User

from models import db, User


class TestLogin:

    def test_login_com_credenciais_validas(self, client, app):
        with app.app_context():
            user = User(nome="Carlos", email="carlos@email.com")
            user.set_password("senha123")
            db.session.add(user)
            db.session.commit()

        response = client.post('/auth/login', data={
            'email': 'carlos@email.com',
            'senha': 'senha123'
        }, follow_redirects=True)

        assert response.status_code == 200

    def test_login_com_senha_errada(self, client, app):
        with app.app_context():
            user = User(nome="Carlos", email="carlos2@email.com")
            user.set_password("senha_certa")
            db.session.add(user)
            db.session.commit()

        response = client.post('/auth/login', data={
            'email': 'carlos2@email.com',
            'senha': 'senha_errada'
        }, follow_redirects=True)

        assert b'incorretos' in response.data

    def test_login_get_retorna_pagina(self, client):
        response = client.get('/auth/login')
        assert response.status_code == 200


class TestCadastro:

    def test_cadastro_com_dados_validos(self, client):
        response = client.post('/auth/cadastro', data={
            'nome': 'Carlos Henrique',
            'email': 'novo@email.com',
            'senha': 'senha123',
            'confirmar_senha': 'senha123'
        }, follow_redirects=True)

        assert response.status_code == 200

    def test_cadastro_com_senhas_diferentes(self, client):
        response = client.post('/auth/cadastro', data={
            'nome': 'Carlos',
            'email': 'carlos@email.com',
            'senha': 'senha123',
            'confirmar_senha': 'senha_diferente'
        }, follow_redirects=True)

        assert b'coincidem' in response.data

    def test_cadastro_com_campos_vazios(self, client):
        response = client.post('/auth/cadastro', data={
            'nome': '',
            'email': '',
            'senha': ''
        }, follow_redirects=True)

        assert b'obrigat' in response.data

    def test_cadastro_com_email_ja_existente(self, client, app):
        with app.app_context():
            user = User(nome="Carlos", email="existente@email.com")
            user.set_password("senha123")
            db.session.add(user)
            db.session.commit()

        response = client.post('/auth/cadastro', data={
            'nome': 'Outro',
            'email': 'existente@email.com',
            'senha': 'senha123',
            'confirmar_senha': 'senha123'
        }, follow_redirects=True)

        assert b'cadastrado' in response.data