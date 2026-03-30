"""
Popula DB com dados de exemplo (desenvolvimento)
"""

import os
from datetime import datetime
from app import create_app
from models import db, User, Product

def init_database(app=None):
    if app is None:
        app = create_app('development')

    # senhas configuráveis via env (evita hardcode em CI/hosts públicos)
    ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', 'admin123')
    TEST_PASSWORD = os.environ.get('TEST_PASSWORD', 'teste123')

    with app.app_context():
        print("Criando tabelas...")
        db.create_all()

        # se já tem dados, pular
        if User.query.first():
            print("Banco de dados já contém dados. Pulando inicialização.")
            return

        print("Populando banco de dados...")

        try:
            # criar admin
            admin = User(
                nome="Administrador",
                email="admin@donshop007.com",
                is_admin=True
            )
            admin.set_password(ADMIN_PASSWORD)
            db.session.add(admin)

            # criar usuário teste
            user_teste = User(
                nome="Cliente Teste",
                email="cliente@teste.com",
                is_admin=False
            )
            user_teste.set_password(TEST_PASSWORD)
            db.session.add(user_teste)

            # produtos de exemplo
            produtos = [
                Product(
                    nome="Caneca Elegante Branca",
                    descricao=("Caneca branca sofisticada com detalhes em dourado rosé. "
                               "Perfeita para personalização. Material cerâmico de alta qualidade."),
                    preco=45.00,
                    categoria="caneca",
                    imagem_url="caneca_1.png",
                    estoque=100
                ),
                Product(
                    nome="Caneca Geométrica Premium",
                    descricao=("Caneca com padrão geométrico elegante em azul marinho e dourado. "
                               "Design moderno e sofisticado."),
                    preco=52.00,
                    categoria="caneca",
                    imagem_url="caneca_2.png",
                    estoque=100
                ),
                Product(
                    nome="Caneca Metálica Rosé",
                    descricao=("Caneca com acabamento metálico em dourado rosé. Luxuosa e elegante."),
                    preco=68.00,
                    categoria="caneca",
                    imagem_url="caneca_3.png",
                    estoque=100
                ),
                Product(
                    nome="Copo Minimalista",
                    descricao="Copo de vidro transparente com design minimalista. Ideal para personalização.",
                    preco=38.00,
                    categoria="copo",
                    imagem_url="copo_1.png",
                    estoque=100
                ),
                Product(
                    nome="Tumbler Térmico Azul",
                    descricao=("Tumbler térmico em azul marinho fosco. Mantém bebidas quentes por 6h "
                               "e frias por 12h. Tampa antivazamento."),
                    preco=55.00,
                    categoria="copo",
                    imagem_url="copo_2.png",
                    estoque=100
                ),
                Product(
                    nome="Copo Decorado Colorido",
                    descricao="Copo de vidro com estampa colorida vibrante. Perfeito para presente.",
                    preco=42.00,
                    categoria="copo",
                    imagem_url="copo_3.png",
                    estoque=100
                ),
                Product(
                    nome="Camiseta Elegante Branca",
                    descricao=("Camiseta branca premium com estampa geométrica. 100% algodão, "
                               "confortável e respirável."),
                    preco=89.00,
                    categoria="camisa",
                    imagem_url="camisa_1.png",
                    estoque=100
                ),
                Product(
                    nome="Camiseta Preta Design",
                    descricao=("Camiseta preta com design geométrico sofisticado. Tecido de alta qualidade."),
                    preco=95.00,
                    categoria="camisa",
                    imagem_url="camisa_2.png",
                    estoque=100
                ),
                Product(
                    nome="Camiseta Artística Clara",
                    descricao=("Camiseta clara com estampa artística exclusiva. 100% algodão premium."),
                    preco=85.00,
                    categoria="camisa",
                    imagem_url="camisa_3.png",
                    estoque=100
                )
            ]

            for p in produtos:
                db.session.add(p)

            # commit final
            db.session.commit()

        except Exception as exc:
            db.session.rollback()
            print("Erro ao inicializar o banco:", exc)
            raise

        # sumário (apenas dev)
        print("\n" + "="*60)
        print("✅ Banco de dados inicializado com sucesso!")
        print("="*60)
        print("\nCREDENCIAIS DE ACESSO (AMBIENTE DE DESENVOLVIMENTO):")
        print("\n📧 ADMIN:")
        print("   Email: admin@donshop007.com")
        print(f"   Senha: {ADMIN_PASSWORD}")
        print("\n👤 USUÁRIO TESTE:")
        print("   Email: cliente@teste.com")
        print(f"   Senha: {TEST_PASSWORD}")
        print("\n📦 PRODUTOS CRIADOS: 9")
        print("   - 3 Canecas")
        print("   - 3 Copos")
        print("   - 3 Camisas")
        print("="*60 + "\n")


if __name__ == '__main__':
    init_database()
