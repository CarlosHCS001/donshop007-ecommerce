# 🛍️ DonShop007 - E-commerce de Produtos Personalizados

**Onde estilo encontra excelência**

E-commerce completo desenvolvido em Python/Flask para venda de produtos personalizados (canecas, copos e camisas).

---

## ⚠️ IMPORTANTE: LEIA PRIMEIRO!

### 📥 Projeto Desenvolvido no DeepAgent

**Este projeto foi desenvolvido no ambiente DeepAgent (servidor remoto).**

Se você está tentando fazer o deploy a partir do **seu computador local**, siga estas instruções:

### ✅ Passos Obrigatórios:

1. **📁 BAIXE TODOS OS ARQUIVOS**
   - Veja instruções detalhadas em: **[INSTRUCOES_DOWNLOAD.md](/home/ubuntu/INSTRUCOES_DOWNLOAD.md)**
   - Clique no botão "Files" no canto superior direito da interface
   - Navegue até `/home/ubuntu/donshop007/`
   - Baixe a pasta completa como ZIP

2. **💾 EXTRAIA NO SEU COMPUTADOR**
   - Windows: `C:\Users\SeuNome\donshop007`
   - Mac/Linux: `~/donshop007`

3. **📖 SIGA O GUIA DE DEPLOY LOCAL**
   - Abra o arquivo: **[GUIA_DEPLOY_LOCAL.md](GUIA_DEPLOY_LOCAL.md)**
   - Siga todos os passos do guia
   - Use os comandos prontos em: **[COMANDOS_RAPIDOS.txt](COMANDOS_RAPIDOS.txt)**

4. **✅ USE O CHECKLIST**
   - Marque seu progresso em: **[CHECKLIST_DOWNLOAD_DEPLOY.md](CHECKLIST_DOWNLOAD_DEPLOY.md)**

5. **🔧 EM CASO DE ERRO**
   - Consulte: **[SOLUCAO_PROBLEMAS.md](SOLUCAO_PROBLEMAS.md)**

### 🚨 Erros Comuns:

**❌ "No such file or directory: /home/ubuntu/donshop007"**
- **Causa:** Você está no computador local, mas o diretório está no DeepAgent
- **Solução:** Baixe os arquivos primeiro (ver instruções acima)

**❌ "git: command not found"**
- **Causa:** Git não está instalado
- **Solução:** Instale o Git: https://git-scm.com/downloads

**❌ "Permission denied"**
- **Causa:** Problema de autenticação com GitHub
- **Solução:** Use token de acesso pessoal (ver GUIA_DEPLOY_LOCAL.md)

### 📚 Documentação Completa:

| Arquivo | Descrição |
|---------|-----------|
| **[INSTRUCOES_DOWNLOAD.md](/home/ubuntu/INSTRUCOES_DOWNLOAD.md)** | Como baixar arquivos do DeepAgent |
| **[GUIA_DEPLOY_LOCAL.md](GUIA_DEPLOY_LOCAL.md)** | Guia completo de deploy local → GitHub → Render |
| **[COMANDOS_RAPIDOS.txt](COMANDOS_RAPIDOS.txt)** | Comandos prontos para copiar e colar |
| **[SOLUCAO_PROBLEMAS.md](SOLUCAO_PROBLEMAS.md)** | Soluções para erros comuns |
| **[CHECKLIST_DOWNLOAD_DEPLOY.md](CHECKLIST_DOWNLOAD_DEPLOY.md)** | Checklist passo a passo |

---

---

## 📋 Sobre o Projeto

Este projeto foi desenvolvido como parte do TCC (Trabalho de Conclusão de Curso) do curso de **Engenharia de Software** da **UniCesumar**, pelo aluno **Carlos Henrique Conceição Soares**, sob orientação da **Profa. Janaina Aparecida**.

O objetivo é demonstrar a aplicação prática dos conceitos de desenvolvimento web, incluindo:
- Arquitetura em camadas (Frontend, Backend, Banco de Dados)
- Metodologia ágil (Scrum)
- Integração de APIs
- Sistema de autenticação
- CRUD completo
- Responsividade e UX

---

## 🎨 Identidade Visual

- **Nome**: DonShop007
- **Slogan**: Onde estilo encontra excelência
- **Logo**: D dourado rosé + S azul marinho em fundo claro
- **Paleta de Cores**:
  - Principal: Azul Marinho Escuro (#0a1929)
  - Secundária: Branco Gelo (#f5f5f5)
  - Destaque: Dourado Rosé (#b76e79)
  - Cinza: (#4a4a4a)
- **Estilo**: Elegante + Minimalista (sofisticação moderna)

---

## 🚀 Funcionalidades

### 👤 Usuário Cliente

- ✅ Cadastro e login de usuários
- ✅ Login social visual (Google, Facebook - apenas interface)
- ✅ Navegação por catálogo de produtos
- ✅ Busca e filtros por categoria
- ✅ Visualização de detalhes do produto
- ✅ Sistema de avaliações (máximo 10 por produto)
- ✅ Carrinho de compras (adicionar, remover, atualizar)
- ✅ Personalização de produtos (texto + imagem)
- ✅ Upload de imagens para personalização
- ✅ Checkout com validação de CEP via API ViaCEP
- ✅ Cálculo de frete por região
- ✅ Pagamento simulado (gateway fake para demonstração)
- ✅ Histórico de pedidos
- ✅ Visualização de detalhes do pedido

### 🔧 Administrador

- ✅ Dashboard com estatísticas
- ✅ Gerenciamento de produtos (CRUD completo)
- ✅ Gerenciamento de pedidos (visualização e alteração de status)
- ✅ Gerenciamento de usuários
- ✅ Gerenciamento de avaliações (visualização e exclusão)
- ✅ Visualização de pedidos recentes

---

## 💻 Tecnologias Utilizadas

### Backend
- **Python 3.11**
- **Flask 3.0** - Framework web
- **SQLAlchemy 2.0** - ORM para banco de dados
- **Flask-Login** - Sistema de autenticação
- **Flask-WTF** - Formulários e validação
- **Flask-Migrate** - Migrations do banco de dados
- **Werkzeug** - Segurança (hash de senhas)

### Frontend
- **HTML5**
- **CSS3** (design customizado)
- **JavaScript** (ES6+)
- **Bootstrap 5.3** - Framework CSS
- **Bootstrap Icons** - Ícones
- **Google Fonts** (Montserrat + Playfair Display)

### Banco de Dados
- **PostgreSQL** - Banco de dados relacional

### Integrações
- **API ViaCEP** - Consulta de CEP e validação de endereço
- **Requests** - Requisições HTTP

### Deploy
- **Gunicorn** - Servidor WSGI para produção
- **Render.com** - Plataforma de deploy

---

## 📦 Estrutura do Projeto

```
donshop007/
├── app.py                 # Aplicação principal Flask
├── config.py              # Configurações do app
├── models.py              # Modelos do banco de dados
├── init_db.py             # Script de inicialização do banco
├── requirements.txt       # Dependências Python
├── Procfile              # Arquivo para deploy Render
├── runtime.txt           # Versão do Python
├── .env.example          # Exemplo de variáveis de ambiente
├── .gitignore            # Arquivos ignorados pelo Git
├── routes/               # Blueprints de rotas
│   ├── __init__.py
│   ├── main.py           # Rotas principais (home, sobre)
│   ├── auth.py           # Autenticação (login, cadastro)
│   ├── products.py       # Produtos (listagem, detalhes, avaliações)
│   ├── cart.py           # Carrinho de compras
│   ├── orders.py         # Pedidos (checkout, pagamento)
│   └── admin.py          # Painel administrativo
├── templates/            # Templates HTML
│   ├── base.html         # Template base
│   ├── index.html        # Homepage
│   ├── sobre.html
│   ├── contato.html
│   ├── auth/             # Templates de autenticação
│   ├── produtos/         # Templates de produtos
│   ├── cart/             # Templates de carrinho
│   ├── orders/           # Templates de pedidos
│   ├── admin/            # Templates admin
│   └── errors/           # Páginas de erro
├── static/               # Arquivos estáticos
│   ├── css/
│   │   └── style.css     # CSS customizado
│   ├── js/
│   │   └── main.js       # JavaScript principal
│   ├── images/           # Imagens (logo e produtos)
│   └── uploads/          # Uploads de usuários
└── README.md             # Este arquivo
```

---

## 🔧 Instalação e Execução Local

### Pré-requisitos

- Python 3.11 ou superior
- PostgreSQL 12 ou superior
- pip (gerenciador de pacotes Python)
- Git

### Passo 1: Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/donshop007.git
cd donshop007
```

### Passo 2: Criar Ambiente Virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Passo 3: Instalar Dependências

```bash
pip install -r requirements.txt
```

### Passo 4: Configurar Banco de Dados PostgreSQL

```bash
# Entrar no PostgreSQL
psql -U postgres

# Criar banco de dados
CREATE DATABASE donshop007;

# Criar usuário (opcional)
CREATE USER donshop_user WITH PASSWORD 'sua_senha';
GRANT ALL PRIVILEGES ON DATABASE donshop007 TO donshop_user;

# Sair
\q
```

### Passo 5: Configurar Variáveis de Ambiente

```bash
# Copiar o arquivo de exemplo
cp .env.example .env

# Editar .env com suas configurações
# Exemplo:
# DATABASE_URL=postgresql://postgres:senha@localhost/donshop007
# SECRET_KEY=sua-chave-secreta-aqui
```

### Passo 6: Inicializar o Banco de Dados

```bash
python init_db.py
```

Este comando irá:
- Criar todas as tabelas
- Popular com 9 produtos
- Criar usuário admin
- Criar usuário de teste

### Passo 7: Executar o Servidor

```bash
python app.py
```

A aplicação estará disponível em: `http://localhost:5000`

---

## 🔐 Credenciais de Teste

### Administrador
- **Email**: admin@donshop007.com
- **Senha**: admin123

### Usuário Teste
- **Email**: cliente@teste.com
- **Senha**: teste123

---

## 📦 Produtos Disponíveis

### Canecas (3 produtos)
1. **Caneca Elegante Branca** - R$ 45,00
2. **Caneca Geométrica Premium** - R$ 52,00
3. **Caneca Metálica Rosé** - R$ 68,00

### Copos (3 produtos)
1. **Copo Minimalista** - R$ 38,00
2. **Tumbler Térmico Azul** - R$ 55,00
3. **Copo Decorado Colorido** - R$ 42,00

### Camisas (3 produtos)
1. **Camiseta Elegante Branca** - R$ 89,00
2. **Camiseta Preta Design** - R$ 95,00
3. **Camiseta Artística Clara** - R$ 85,00

---

## 🌐 Deploy e Publicação

### 📚 Guias Completos de Deploy

Este projeto inclui guias detalhados passo a passo para publicar o e-commerce:

1. **[GUIA_GITHUB.md](GUIA_GITHUB.md)** 📘
   - Como criar conta no GitHub
   - Como criar repositório público
   - Como configurar Git localmente
   - Como fazer commit e push do código
   - Comandos prontos para copiar e colar

2. **[GUIA_RENDER.md](GUIA_RENDER.md)** 🚀
   - Como criar conta no Render.com
   - Como criar banco de dados PostgreSQL gratuito
   - Como fazer deploy do Web Service
   - Como configurar variáveis de ambiente
   - Como popular o banco de dados
   - Troubleshooting e soluções de problemas

3. **[CHECKLIST_DEPLOY.md](CHECKLIST_DEPLOY.md)** ✅
   - Checklist interativo para acompanhar progresso
   - Lista de verificação completa
   - Espaço para anotar URLs importantes

4. **[PROXIMOS_PASSOS.md](PROXIMOS_PASSOS.md)** 📋
   - Resumo executivo do que fazer
   - Tempo estimado para cada etapa
   - Links rápidos para os guias

### 🎯 Resumo Rápido do Deploy

**Tempo total estimado**: 30-40 minutos

1. **GitHub** (10-15 min)
   - Criar repositório público
   - Fazer push do código

2. **Render.com** (20-25 min)
   - Criar banco PostgreSQL
   - Criar Web Service
   - Configurar variáveis de ambiente
   - Executar init_db.py

3. **Teste** (5 min)
   - Acessar site publicado
   - Testar funcionalidades principais

### 🔗 Links do Projeto

Após o deploy, anote aqui as URLs:

- **Site em Produção**: `https://seu-app.onrender.com`
- **Repositório GitHub**: `https://github.com/seu-usuario/donshop007-ecommerce`
- **Dashboard Render**: `https://dashboard.render.com`

### ⚡ Deploy Rápido (Para Experientes)

Se você já conhece Git e Render:

```bash
# 1. GitHub
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/SEU-USERNAME/donshop007-ecommerce.git
git push -u origin main

# 2. Render.com
# - Criar PostgreSQL (copiar DATABASE_URL)
# - Criar Web Service conectado ao GitHub
# - Adicionar env vars: SECRET_KEY, DATABASE_URL, FLASK_ENV=production
# - Aguardar deploy
# - Executar no Shell: python init_db.py
```

---

## 🧪 Testes e Validação

### Fluxo de Teste Completo

1. **Cadastro de Usuário**
   - Acesse `/auth/cadastro`
   - Crie uma conta com email e senha

2. **Login**
   - Faça login com as credenciais criadas

3. **Navegação de Produtos**
   - Explore o catálogo
   - Filtre por categoria
   - Use a busca

4. **Adicionar ao Carrinho**
   - Selecione um produto
   - Clique em "Adicionar ao Carrinho"

5. **Personalização** (Opcional)
   - No carrinho, adicione texto personalizado
   - Faça upload de uma imagem

6. **Checkout**
   - Preencha dados de entrega
   - Digite um CEP válido (consulta automática via ViaCEP)
   - Veja o cálculo do frete

7. **Pagamento**
   - Preencha dados do cartão (simulado)
   - Confirme o pagamento

8. **Confirmação**
   - Veja detalhes do pedido confirmado

9. **Avaliação**
   - Acesse um produto já comprado
   - Deixe uma avaliação (nota + comentário)

10. **Painel Admin** (com usuário admin)
    - Acesse `/admin`
    - Gerencie produtos, pedidos, usuários

---

## 📊 Modelos de Dados

### User (Usuário)
- id, nome, email, senha_hash, is_admin, created_at

### Product (Produto)
- id, nome, descricao, preco, categoria, imagem_url, estoque, created_at

### Review (Avaliação)
- id, product_id, user_id, rating, comentario, created_at

### Order (Pedido)
- id, user_id, total, frete, status, nome_destinatario, cep, endereco, numero, complemento, bairro, cidade, estado, created_at, updated_at

### OrderItem (Item do Pedido)
- id, order_id, product_id, quantidade, preco_unitario, personalizacao_texto, personalizacao_imagem

### Cart (Carrinho)
- id, user_id, created_at

### CartItem (Item do Carrinho)
- id, cart_id, product_id, quantidade, personalizacao_texto, personalizacao_imagem

---

## 🔒 Segurança

- Senhas armazenadas com hash (Werkzeug)
- Proteção CSRF em formulários
- Validação de dados no backend
- Sanitização de inputs
- Upload de arquivos com validação de extensão e tamanho
- Sessões seguras com cookies HTTP-only

---

## 📝 Observações Importantes

### Localhost
⚠️ **IMPORTANTE**: Este localhost refere-se ao localhost do computador onde o DeepAgent está executando a aplicação, não sua máquina local. Para acessar localmente ou remotamente, você precisará fazer o deploy da aplicação em seu próprio sistema.

### Login Social
Os botões de login social (Google, Facebook) são apenas visuais para demonstração. Não estão funcionalmente implementados.

### Gateway de Pagamento
O sistema de pagamento é simulado para fins de demonstração. Não processa pagamentos reais.

### API de Frete
O cálculo de frete é simplificado por região (Sul, Sudeste, Nordeste, Norte, Centro-Oeste) através de consulta ao ViaCEP.

---

## 🐛 Resolução de Problemas

### Erro de Conexão com PostgreSQL
```bash
# Verifique se o PostgreSQL está rodando
sudo service postgresql status

# Verifique a string de conexão no .env
DATABASE_URL=postgresql://usuario:senha@localhost/donshop007
```

### Erro ao Instalar psycopg2
```bash
# Ubuntu/Debian
sudo apt-get install libpq-dev python3-dev

# Windows - Use psycopg2-binary (já está no requirements.txt)
```

### Erro 404 em Imagens
```bash
# Verifique se as imagens estão em static/images/
ls static/images/
```

---

## 📚 Documentação Adicional

### APIs Utilizadas

**ViaCEP**
- Endpoint: `https://viacep.com.br/ws/{cep}/json/`
- Método: GET
- Sem autenticação
- Gratuito

### Estrutura de Rotas

- `/` - Homepage
- `/produtos` - Listagem de produtos
- `/produtos/<id>` - Detalhes do produto
- `/auth/login` - Login
- `/auth/cadastro` - Cadastro
- `/auth/logout` - Logout
- `/carrinho` - Carrinho de compras
- `/pedidos/checkout` - Checkout
- `/pedidos/meus-pedidos` - Histórico de pedidos
- `/admin` - Painel administrativo

---

## 👨‍💻 Autor

**Carlos Henrique Conceição Soares**
- Curso: Engenharia de Software
- Instituição: UniCesumar
- Orientadora: Profa. Janaina Aparecida
- Data: Novembro/2024

---

## 📄 Licença

Este projeto foi desenvolvido para fins acadêmicos como parte do TCC do curso de Engenharia de Software da UniCesumar.

---

## 🙏 Agradecimentos

- Profa. Janaina Aparecida pela orientação
- UniCesumar pelo suporte acadêmico
- Comunidade Flask e Python pela excelente documentação
- Bootstrap pela framework CSS
- Render.com pela plataforma de deploy gratuita

---

## 📞 Contato

Para dúvidas ou sugestões sobre o projeto:
- Email: contato@donshop007.com (fictício)

---

**DonShop007 - Onde estilo encontra excelência** ✨
