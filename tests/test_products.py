from models import db, Product, User


class TestProdutos:

    def _criar_produto(self, session):
        produto = Product(
            nome="Caneca Teste",
            descricao="Caneca de teste",
            preco=49.90,
            categoria="caneca",
            imagem_url="/img/caneca.jpg",
            estoque=10
        )
        session.add(produto)
        session.commit()
        return produto

    def test_listar_produtos_retorna_200(self, client):
        response = client.get('/produtos/')
        assert response.status_code == 200

    def test_listar_com_filtro_categoria(self, client):
        response = client.get('/produtos/?categoria=caneca')
        assert response.status_code == 200

    def test_listar_com_busca(self, client):
        response = client.get('/produtos/?busca=caneca')
        assert response.status_code == 200

    def test_detalhe_produto_existente(self, client, app):
        with app.app_context():
            produto = self._criar_produto(db.session)
            produto_id = produto.id

        response = client.get(f'/produtos/{produto_id}')
        assert response.status_code == 200

    def test_detalhe_produto_inexistente_retorna_404(self, client):
        response = client.get('/produtos/9999')
        assert response.status_code == 404

    def test_avaliar_sem_login_redireciona(self, client, app):
        with app.app_context():
            produto = self._criar_produto(db.session)
            produto_id = produto.id

        response = client.post(f'/produtos/{produto_id}/avaliar', data={
            'rating': '5',
            'comentario': 'Ótimo produto'
        })
        assert response.status_code == 302

    def test_listar_com_ordenacao(self, client):
        response = client.get('/produtos/?ordem=menor_preco')
        assert response.status_code == 200