from models import db, Product, User, Cart, CartItem


class TestCarrinho:

    def _criar_usuario_e_logar(self, client, app):
        with app.app_context():
            user = User(nome="Carlos", email="cart@email.com")
            user.set_password("senha123")
            db.session.add(user)
            db.session.commit()

        client.post('/auth/login', data={
            'email': 'cart@email.com',
            'senha': 'senha123'
        }, follow_redirects=True)

    def _criar_produto(self, session):
        produto = Product(
            nome="Caneca Cart",
            descricao="Teste",
            preco=49.90,
            categoria="caneca",
            imagem_url="/img/caneca.jpg",
            estoque=10
        )
        session.add(produto)
        session.commit()
        return produto

    def test_ver_carrinho_sem_login_redireciona(self, client):
        response = client.get('/carrinho/')
        assert response.status_code == 302

    def test_ver_carrinho_com_login(self, client, app):
        self._criar_usuario_e_logar(client, app)
        response = client.get('/carrinho/', follow_redirects=True)
        assert response.status_code == 200

    def test_adicionar_sem_login_redireciona(self, client):
        response = client.post('/carrinho/adicionar/1')
        assert response.status_code == 302

    def test_adicionar_produto_com_login(self, client, app):
        self._criar_usuario_e_logar(client, app)
        with app.app_context():
            produto = self._criar_produto(db.session)
            produto_id = produto.id

        response = client.post(f'/carrinho/adicionar/{produto_id}', data={
            'quantidade': '1'
        }, follow_redirects=True)
        assert response.status_code == 200

    def test_limpar_carrinho_com_login(self, client, app):
        self._criar_usuario_e_logar(client, app)
        response = client.post('/carrinho/limpar', follow_redirects=True)
        assert response.status_code == 200