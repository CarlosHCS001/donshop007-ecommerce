"""
Script para inicializar o banco de dados com dados de exemplo
"""
from app import create_app
from models import db, User, Product
from datetime import datetime

def init_database():
    """Inicializa o banco de dados com dados de exemplo"""
    
    app = create_app('development')
    
    with app.app_context():
        # Criar todas as tabelas
        print("Criando tabelas...")
        db.create_all()
        
        # Verificar se já existem dados
        if User.query.first():
            print("Banco de dados já contém dados. Pulando inicialização.")
            return
        
        print("Populando banco de dados...")
        
        # Criar usuário admin
        admin = User(
            nome="Administrador",
            email="admin@donshop007.com",
            is_admin=True
        )
        admin.set_password("admin123")
        db.session.add(admin)
        
        # Criar usuário teste
        user_teste = User(
            nome="Cliente Teste",
            email="cliente@teste.com",
            is_admin=False
        )
        user_teste.set_password("teste123")
        db.session.add(user_teste)
        
        # Criar produtos - CANECAS
        produtos = [
            Product(
                nome="Caneca Elegante Branca",
                descricao="Caneca branca sofisticada com detalhes em dourado rosé. Perfeita para personalização com seu nome ou frase favorita. Material cerâmico de alta qualidade.",
                preco=45.00,
                categoria="caneca",
                imagem_url="caneca_1.png",
                estoque=100
            ),
            Product(
                nome="Caneca Geométrica Premium",
                descricao="Caneca com padrão geométrico elegante em azul marinho e dourado. Design moderno e sofisticado, ideal para quem aprecia estilo.",
                preco=52.00,
                categoria="caneca",
                imagem_url="caneca_2.png",
                estoque=100
            ),
            Product(
                nome="Caneca Metálica Rosé",
                descricao="Caneca com acabamento metálico em dourado rosé. Luxuosa e elegante, perfeita para momentos especiais. Mantém a temperatura por mais tempo.",
                preco=68.00,
                categoria="caneca",
                imagem_url="caneca_3.png",
                estoque=100
            ),
            # COPOS
            Product(
                nome="Copo Minimalista",
                descricao="Copo de vidro transparente com design minimalista e elegante. Perfeito para personalizar com iniciais ou pequenos desenhos.",
                preco=38.00,
                categoria="copo",
                imagem_url="copo_1.png",
                estoque=100
            ),
            Product(
                nome="Tumbler Térmico Azul",
                descricao="Tumbler térmico em azul marinho fosco. Mantém bebidas quentes por 6h e frias por 12h. Tampa antivazamento incluída.",
                preco=55.00,
                categoria="copo",
                imagem_url="copo_2.png",
                estoque=100
            ),
            Product(
                nome="Copo Decorado Colorido",
                descricao="Copo de vidro com estampa colorida vibrante. Design alegre e único, perfeito para presentear ou uso diário.",
                preco=42.00,
                categoria="copo",
                imagem_url="copo_3.png",
                estoque=100
            ),
            # CAMISAS
            Product(
                nome="Camiseta Elegante Branca",
                descricao="Camiseta branca premium com estampa geométrica em azul e dourado. 100% algodão, confortável e respirável. Ideal para personalização.",
                preco=89.00,
                categoria="camisa",
                imagem_url="camisa_1.png",
                estoque=100
            ),
            Product(
                nome="Camiseta Preta Design",
                descricao="Camiseta preta com design geométrico sofisticado. Tecido de alta qualidade com toque macio. Estilo urbano e moderno.",
                preco=95.00,
                categoria="camisa",
                imagem_url="camisa_2.png",
                estoque=100
            ),
            Product(
                nome="Camiseta Artística Clara",
                descricao="Camiseta em tom claro com estampa artística exclusiva. Design único que combina elegância e criatividade. 100% algodão premium.",
                preco=85.00,
                categoria="camisa",
                imagem_url="camisa_3.png",
                estoque=100
            )
        ]
        
        for produto in produtos:
            db.session.add(produto)
        
        # Commit no banco
        db.session.commit()
        
        print("\n" + "="*60)
        print("✅ Banco de dados inicializado com sucesso!")
        print("="*60)
        print("\nCREDENCIAIS DE ACESSO:")
        print("\n📧 ADMIN:")
        print("   Email: admin@donshop007.com")
        print("   Senha: admin123")
        print("\n👤 USUÁRIO TESTE:")
        print("   Email: cliente@teste.com")
        print("   Senha: teste123")
        print("\n📦 PRODUTOS CRIADOS: 9")
        print("   - 3 Canecas")
        print("   - 3 Copos")
        print("   - 3 Camisas")
        print("="*60 + "\n")

if __name__ == '__main__':
    init_database()
