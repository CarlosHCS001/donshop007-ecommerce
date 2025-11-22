# 🚀 GUIA COMPLETO: Deploy do DonShop007 a partir do Computador Local

## ⚠️ LEIA ISTO PRIMEIRO!

**O projeto DonShop007 foi desenvolvido no DeepAgent (servidor remoto).**  
Os arquivos **NÃO estão no seu computador** ainda. Você precisa baixá-los primeiro!

---

## 📋 PASSO 1: BAIXAR OS ARQUIVOS DO DEEPAGENT

### Como baixar:

1. **Localize o botão "Files"** no canto superior direito da interface do DeepAgent
   - É um ícone de pasta ou texto escrito "Files"

2. **Navegue até a pasta do projeto:**
   - Clique em "Files"
   - Procure e acesse: `/home/ubuntu/donshop007/`

3. **Baixe todos os arquivos:**
   
   **Opção A - Baixar pasta completa (Recomendado):**
   - Clique com botão direito na pasta `donshop007`
   - Selecione "Download" ou "Download as ZIP"
   - Salve o arquivo ZIP no seu computador
   
   **Opção B - Baixar arquivos individualmente:**
   - Selecione todos os arquivos dentro da pasta
   - Clique em "Download" ou "Download Selected"

4. **Extraia os arquivos:**
   
   **Windows:**
   - Clique com botão direito no arquivo ZIP
   - Escolha "Extrair tudo..." ou "Extract here"
   - Extraia para: `C:\Users\SeuNome\donshop007`
   
   **Mac:**
   - Clique duas vezes no arquivo ZIP
   - Mova a pasta extraída para: `~/Documents/donshop007`
   
   **Linux:**
   ```bash
   unzip donshop007.zip -d ~/donshop007
   ```

---

## 📂 PASSO 2: VERIFICAR OS ARQUIVOS

### Abra o terminal na pasta extraída:

**Windows:**
1. Abra o Explorador de Arquivos
2. Navegue até `C:\Users\SeuNome\donshop007`
3. Na barra de endereços, digite `cmd` e pressione Enter
4. Ou clique com botão direito e escolha "Open PowerShell here"

**Mac:**
1. Abra o Finder
2. Navegue até a pasta `donshop007`
3. Clique com botão direito e escolha "New Terminal at Folder"

**Linux:**
1. Navegue até a pasta no gerenciador de arquivos
2. Clique com botão direito e escolha "Open Terminal Here"

### Verifique se os arquivos estão presentes:

```bash
# Windows (PowerShell/CMD)
dir

# Mac/Linux
ls -la
```

### Arquivos importantes que devem estar presentes:

✅ **Arquivos principais:**
- `server.js` - Servidor principal
- `package.json` - Dependências do projeto
- `.env.example` - Exemplo de variáveis de ambiente
- `README.md` - Documentação do projeto

✅ **Pastas:**
- `public/` - Arquivos estáticos (CSS, JS, imagens)
- `views/` - Templates HTML (EJS)
- `data/` - Banco de dados JSON

✅ **Arquivos de configuração:**
- `.gitignore` - Arquivos ignorados pelo Git
- `render.yaml` - Configuração do Render.com

Se algum arquivo importante estiver faltando, **volte ao Passo 1** e baixe novamente!

---

## 🔧 PASSO 3: CONFIGURAR GIT LOCALMENTE

### 3.1 - Verificar se o Git está instalado:

```bash
git --version
```

**Se aparecer erro "git não encontrado":**

- **Windows:** Baixe em https://git-scm.com/download/win
- **Mac:** Execute `brew install git` (se tiver Homebrew) ou baixe em https://git-scm.com/download/mac
- **Linux:** `sudo apt install git` (Ubuntu/Debian) ou `sudo yum install git` (RedHat/CentOS)

### 3.2 - Configurar seu usuário Git (primeira vez):

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu.email@example.com"
```

⚠️ **Use o mesmo email da sua conta GitHub!**

### 3.3 - Inicializar repositório Git:

```bash
# Navegue até a pasta do projeto (se ainda não estiver nela)
cd donshop007

# Inicialize o Git
git init

# Verifique o status
git status
```

### 3.4 - Adicionar arquivos ao Git:

```bash
# Adicione todos os arquivos
git add .

# Faça o primeiro commit
git commit -m "Initial commit - DonShop007 E-commerce"
```

---

## 🌐 PASSO 4: CRIAR REPOSITÓRIO NO GITHUB

### 4.1 - Criar repositório:

1. Acesse https://github.com
2. Faça login na sua conta
3. Clique no botão **"+" (New repository)** no canto superior direito
4. Ou acesse: https://github.com/new

### 4.2 - Configurar o repositório:

**Nome do repositório:** `donshop007-ecommerce` (ou outro nome de sua preferência)

**Descrição:** `E-commerce DonShop007 - Loja online de produtos eletrônicos`

**Visibilidade:**
- ✅ **Public** (recomendado para projetos pessoais/portfólio)
- ⚪ Private (se quiser manter privado)

⚠️ **IMPORTANTE:**
- **NÃO marque** "Add a README file"
- **NÃO marque** "Add .gitignore"
- **NÃO marque** "Choose a license"

(Esses arquivos já existem no projeto!)

4. Clique em **"Create repository"**

### 4.3 - Conectar repositório local ao GitHub:

Após criar o repositório, o GitHub mostrará instruções. Use estes comandos:

```bash
# Adicione o repositório remoto
git remote add origin https://github.com/SeuUsuario/donshop007-ecommerce.git

# Verifique se foi adicionado corretamente
git remote -v

# Renomeie a branch para 'main' (se necessário)
git branch -M main

# Faça o push do código
git push -u origin main
```

⚠️ **Substitua `SeuUsuario` pelo seu nome de usuário do GitHub!**

### 4.4 - Autenticação:

O GitHub pedirá suas credenciais:

**Opção A - Token de Acesso Pessoal (Recomendado):**
1. Acesse: https://github.com/settings/tokens
2. Clique em "Generate new token" → "Generate new token (classic)"
3. Marque a opção **"repo"** (acesso completo aos repositórios)
4. Clique em "Generate token"
5. **COPIE O TOKEN** (você só verá uma vez!)
6. Use o token como senha quando o Git solicitar

**Opção B - GitHub CLI:**
```bash
# Instale o GitHub CLI
# Windows: winget install --id GitHub.cli
# Mac: brew install gh
# Linux: sudo apt install gh

# Faça login
gh auth login
```

---

## 🚀 PASSO 5: DEPLOY NO RENDER.COM

### 5.1 - Criar conta no Render:

1. Acesse https://render.com
2. Clique em **"Get Started"**
3. Escolha **"Sign up with GitHub"** (mais fácil!)
4. Autorize o Render a acessar sua conta GitHub

### 5.2 - Criar novo Web Service:

1. No dashboard do Render, clique em **"New +"**
2. Selecione **"Web Service"**
3. Clique em **"Connect a repository"**
4. Procure e selecione `donshop007-ecommerce` (ou o nome que você deu)
5. Clique em **"Connect"**

### 5.3 - Configurar o Web Service:

**Name:** `donshop007` (ou outro nome único)

**Region:** `Oregon (US West)` (ou o mais próximo de você)

**Branch:** `main`

**Root Directory:** (deixe vazio)

**Runtime:** `Node`

**Build Command:** 
```bash
npm install
```

**Start Command:**
```bash
node server.js
```

**Instance Type:** `Free` (para começar)

### 5.4 - Configurar Variáveis de Ambiente:

Role a página até **"Environment Variables"** e adicione:

| Key | Value |
|-----|-------|
| `PORT` | `10000` |
| `NODE_ENV` | `production` |
| `SESSION_SECRET` | `sua-chave-secreta-aqui-123456` |

⚠️ **Para `SESSION_SECRET`:** Use uma string aleatória e segura!  
Você pode gerar uma em: https://randomkeygen.com/

### 5.5 - Finalizar Deploy:

1. Role até o final da página
2. Clique em **"Create Web Service"**
3. O Render iniciará o processo de build e deploy automaticamente
4. Aguarde 2-5 minutos (você verá os logs em tempo real)
5. Quando finalizar, você verá: **"Your service is live"** 🎉

### 5.6 - Acessar seu site:

Seu site estará disponível em:
```
https://donshop007.onrender.com
```
(ou o nome que você escolheu)

---

## ✅ VERIFICAÇÃO FINAL

### Teste seu site:

1. **Página Inicial:** Deve carregar com produtos
2. **Login:** Crie uma conta de teste
3. **Carrinho:** Adicione produtos e teste o checkout
4. **Admin:** Acesse `/admin` (se aplicável)

### Se algo não funcionar:

1. Verifique os **logs no Render** (aba "Logs")
2. Confira as **variáveis de ambiente**
3. Veja o arquivo `SOLUCAO_PROBLEMAS.md`
4. Teste localmente primeiro: `npm install && node server.js`

---

## 🔄 ATUALIZAÇÕES FUTURAS

### Para fazer mudanças no projeto:

1. **Edite os arquivos localmente** (no seu computador)
2. **Teste localmente:**
   ```bash
   node server.js
   # Acesse http://localhost:3000
   ```
3. **Faça commit das mudanças:**
   ```bash
   git add .
   git commit -m "Descrição das mudanças"
   git push origin main
   ```
4. **O Render fará deploy automaticamente!** (Auto-deploy)

---

## 📚 ARQUIVOS DE AJUDA

- `COMANDOS_RAPIDOS.txt` - Comandos prontos para copiar
- `SOLUCAO_PROBLEMAS.md` - Soluções para erros comuns
- `INSTRUCOES_DOWNLOAD.md` - Detalhes sobre como baixar do DeepAgent
- `CHECKLIST_DOWNLOAD_DEPLOY.md` - Checklist passo a passo

---

## 💡 DICAS IMPORTANTES

✅ **Sempre teste localmente antes de fazer push**
✅ **Não compartilhe seu SESSION_SECRET publicamente**
✅ **Mantenha backups dos arquivos importantes**
✅ **Use commits descritivos** (ex: "Adiciona filtro de busca")
✅ **Configure auto-deploy no Render** (já vem ativo por padrão)

---

## 🆘 PRECISA DE AJUDA?

- 📖 Documentação do Render: https://render.com/docs
- 📖 Documentação do Git: https://git-scm.com/doc
- 📖 GitHub Guides: https://guides.github.com/

---

**Boa sorte com seu deploy! 🚀**
