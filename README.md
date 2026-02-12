# 🛍️ DonShop007

> **Onde estilo encontra excelência**

E-commerce de produtos personalizados desenvolvido como Trabalho de Conclusão de Curso (TCC) do curso de Engenharia de Software da UniCesumar.

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0-green?logo=flask)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple?logo=bootstrap)
![SQLite](https://img.shields.io/badge/SQLite-3-blue?logo=sqlite)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Ready-blue?logo=postgresql)

---

## 📋 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [Funcionalidades](#-funcionalidades)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Instalação e Configuração](#-instalação-e-configuração)
- [Como Executar](#-como-executar)
- [Credenciais de Teste](#-credenciais-de-teste)
- [Deploy](#-deploy)
- [Screenshots](#-screenshots)
- [Autor](#-autor)

---

## 📖 Sobre o Projeto

O **DonShop007** é uma aplicação web de e-commerce especializada em produtos personalizados, incluindo canecas, copos e camisas. O sistema permite que clientes naveguem pelo catálogo, personalizem produtos com texto e imagens, e finalizem compras com cálculo automático de frete.

O projeto foi desenvolvido para demonstrar as diversas etapas necessárias para o desenvolvimento de um website completo e funcional, abordando desde o backend até o frontend.

---

## ✨ Funcionalidades

### 👤 Área do Cliente
- Cadastro e autenticação de usuários
- Navegação por catálogo de produtos
- Filtros por categoria (canecas, copos, camisas)
- Sistema de busca de produtos
- Carrinho de compras
- Personalização de produtos (texto e imagem)
- Checkout com cálculo automático de frete (API ViaCEP)
- Histórico de pedidos
- Sistema de avaliações e reviews

### 🔧 Painel Administrativo
- Dashboard com estatísticas
- Gerenciamento de produtos (CRUD)
- Gerenciamento de pedidos
- Atualização de status de pedidos
- Gerenciamento de usuários
- Moderação de avaliações
- Controle de estoque

### 🛡️ Segurança
- Senhas criptografadas (Werkzeug)
- Proteção de rotas com decorators
- Validação de formulários
- Controle de acesso por perfil (admin/cliente)

---

## 🛠️ Tecnologias Utilizadas

### Backend
- **Python 3.11** - Linguagem de programação
- **Flask 3.0** - Framework web
- **SQLAlchemy** - ORM para banco de dados
- **Flask-Login** - Gerenciamento de sessões
- **Flask-Migrate** - Migrações de banco de dados
- **Flask-WTF** - Formulários e proteção CSRF

### Frontend
- **HTML5** - Estrutura das páginas
- **CSS3** - Estilização customizada
- **Bootstrap 5.3** - Framework CSS responsivo
- **JavaScript** - Interatividade
- **Bootstrap Icons** - Ícones
- **Google Fonts** - Tipografia (Montserrat, Playfair Display)

### Banco de Dados
- **SQLite** - Desenvolvimento local
- **PostgreSQL** - Produção (Render)

### APIs Externas
- **ViaCEP** - Consulta de CEP e cálculo de frete

---

## 📁 Estrutura do Projeto

```
e-commerce/
├── app.py                 # Aplicação principal Flask
├── config.py              # Configurações do projeto
├── models.py              # Modelos do banco de dados
├── init_db.py             # Script de inicialização do banco
├── requirements.txt       # Dependências Python
├── runtime.txt            # Versão do Python (Render)
├── Procfile               # Comando de execução (Render)
├── .env                   # Variáveis de ambiente (local)
├── .env.example           # Exemplo de variáveis de ambiente
│
├── routes/                # Blueprints (rotas)
│   ├── __init__.py
│   ├── main.py            # Rotas principais (home, sobre, contato)
│   ├── auth.py            # Autenticação (login, cadastro, logout)
│   ├── products.py        # Produtos (listagem, detalhes, avaliações)
│   ├── cart.py            # Carrinho de compras
│   ├── orders.py          # Pedidos (checkout, pagamento, histórico)
│   └── admin.py           # Painel administrativo
│
├── templates/             # Templates HTML (Jinja2)
│   ├── base.html          # Template base
│   ├── index.html         # Página inicial
│   ├── sobre.html         # Página sobre
│   ├── contato.html       # Página de contato
│   ├── auth/              # Templates de autenticação
│   ├── produtos/          # Templates de produtos
│   ├── cart/              # Templates do carrinho
│   ├── orders/            # Templates de pedidos
│   ├── admin/             # Templates administrativos
│   └── errors/            # Páginas de erro (404, 500)
│
├── static/                # Arquivos estáticos
│   ├── css/
│   │   └── style.css      # Estilos customizados
│   ├── js/
│   │   └── main.js        # JavaScript principal
│   └── images/            # Imagens e logos
│
└── instance/              # Banco de dados SQLite (gerado)
    └── donshop007.db
```

---

## 🚀 Instalação e Configuração

### Pré-requisitos
- Python 3.11 ou superior
- pip (gerenciador de pacotes)
- Git

### Passo a Passo

1. **Clone o repositório**
```bash
git clone https://github.com/seu-usuario/donshop007.git
cd donshop007
```

2. **Crie um ambiente virtual**
```bash
python -m venv .venv
```

3. **Ative o ambiente virtual**

Windows:
```bash
.venv\Scripts\activate
```

Linux/Mac:
```bash
source .venv/bin/activate
```

4. **Instale as dependências**
```bash
pip install -r requirements.txt
```

5. **Configure as variáveis de ambiente**
```bash
cp .env.example .env
```

Edite o arquivo `.env`:
```env
SECRET_KEY=sua-chave-secreta-aqui
FLASK_ENV=development
DATABASE_URL=sqlite:///donshop007.db
```

6. **Inicialize o banco de dados**
```bash
python init_db.py
```

---

## ▶️ Como Executar

### Desenvolvimento (local)
```bash
python app.py
```

Acesse: **http://localhost:5000**

### Produção (Gunicorn)
```bash
gunicorn app:app
```

---

## 🔑 Credenciais de Teste

Após executar `init_db.py`, você terá acesso às seguintes contas:

| Tipo | Email | Senha |
|------|-------|-------|
| **Administrador** | admin@donshop007.com | admin123 |
| **Cliente** | cliente@teste.com | teste123 |

---

## 🌐 Deploy

### Render (Recomendado)

1. Crie uma conta no [Render](https://render.com)

2. Crie um novo **Web Service** conectado ao seu repositório GitHub

3. Configure:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`

4. Adicione as variáveis de ambiente:
   - `SECRET_KEY` - Chave secreta para sessões
   - `FLASK_ENV` - `production`
   - `DATABASE_URL` - URL do PostgreSQL (Render fornece)

5. Crie um banco **PostgreSQL** no Render e vincule ao Web Service

---

## 📸 Screenshots

### Página Inicial
*<img width="1302" height="768" alt="unnamed" src="https://github.com/user-attachments/assets/8075b572-5019-4cc4-9855-67a512d6a99e" />


### Catálogo de Produtos
* <img width="1221" height="819" alt="unnamed" src="https://github.com/user-attachments/assets/ae40bf40-6187-4111-8957-2d0b496ce022" />
 *

### Carrinho de Compras
* <img width="1192" height="838" alt="unnamed" src="https://github.com/user-attachments/assets/0ca2164d-a840-479d-a1fc-8d4753882a0d" />
  "

### Painel Administrativo
*<img width="1215" height="823" alt="unnamed" src="https://github.com/user-attachments/assets/ce758fe5-e794-4703-9937-1cbfcd5d3c1d" />
*

---

## 🎨 Paleta de Cores

| Cor | Hex | Uso |
|-----|-----|-----|
| Azul Marinho | `#0a1929` | Navbar, Footer, Títulos |
| Branco Gelo | `#f5f5f5` | Background |
| Dourado Rosé | `#b76e79` | Botões, Destaques |
| Cinza | `#4a4a4a` | Textos |

---

## 📝 Licença

Este projeto foi desenvolvido para fins acadêmicos como parte do TCC do curso de Engenharia de Software.

---

## 👨‍💻 Autor

**Carlos Henrique**

Engenharia de Software - UniCesumar

---

## 🙏 Agradecimentos

- UniCesumar pelo suporte acadêmico
- Professores e orientadores
- Comunidade Flask e Python

---

<p align="center">
  Desenvolvido com ❤️ por Carlos Henrique
</p>
