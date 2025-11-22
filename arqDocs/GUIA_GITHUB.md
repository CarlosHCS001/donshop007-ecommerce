# 📘 Guia Completo: Publicar Projeto no GitHub

Este guia vai te ensinar passo a passo como colocar o projeto DonShop007 no GitHub.

---

## 📋 Pré-requisitos

- Computador com acesso à internet
- Projeto DonShop007 na pasta `/home/ubuntu/donshop007/`
- 15-20 minutos de tempo

---

## 🎯 Passo 1: Criar Conta no GitHub (se não tiver)

### 1.1 Acessar o GitHub
1. Abra seu navegador
2. Acesse: **https://github.com**
3. Clique no botão **"Sign up"** (Cadastrar-se) no canto superior direito

### 1.2 Preencher o Cadastro
1. **Email**: Digite seu melhor email
2. **Password**: Crie uma senha forte (mínimo 8 caracteres)
3. **Username**: Escolha um nome de usuário único (ex: `donshop007`, `seu-nome-dev`)
4. Resolva o puzzle de verificação
5. Clique em **"Create account"**

### 1.3 Verificar Email
1. Abra seu email
2. Procure por email do GitHub
3. Clique no link de verificação
4. Pronto! Conta criada ✅

> **💡 Dica**: Anote seu username do GitHub, você vai precisar dele!

---

## 🎯 Passo 2: Criar Repositório no GitHub

### 2.1 Acessar Página de Novo Repositório
1. Faça login no GitHub (https://github.com/login)
2. Clique no botão **"+"** no canto superior direito
3. Selecione **"New repository"**

### 2.2 Configurar o Repositório
Preencha os campos conforme abaixo:

| Campo | Valor | Descrição |
|-------|-------|-----------|
| **Repository name** | `donshop007-ecommerce` | Nome do seu repositório |
| **Description** | `E-commerce completo desenvolvido com Flask e PostgreSQL` | Descrição opcional |
| **Visibility** | ✅ **Public** | Deixe público para deploy gratuito |
| **Initialize repository** | ❌ NÃO marque nada | Já temos o código pronto |

### 2.3 Criar o Repositório
1. Clique no botão verde **"Create repository"**
2. Você será redirecionado para a página do repositório vazio
3. **IMPORTANTE**: Deixe essa página aberta, vamos precisar dela!

### 2.4 Copiar URL do Repositório
Na página que abriu, você verá uma URL parecida com:
```
https://github.com/SEU-USERNAME/donshop007-ecommerce.git
```

**Copie essa URL completa!** Vamos usar no próximo passo.

---

## 🎯 Passo 3: Configurar Git no Seu Computador

### 3.1 Abrir Terminal
- **Linux/Mac**: Abra o Terminal
- **Windows**: Abra o Git Bash (se não tiver, baixe em https://git-scm.com)

### 3.2 Configurar Seu Nome e Email
Cole esses comandos no terminal (substitua pelos seus dados):

```bash
git config --global user.name "Seu Nome Completo"
git config --global user.email "seu-email@exemplo.com"
```

**Exemplo real:**
```bash
git config --global user.name "João Silva"
git config --global user.email "joao.silva@gmail.com"
```

### 3.3 Verificar Configuração
```bash
git config --global --list
```

Você deve ver seu nome e email listados. ✅

---

## 🎯 Passo 4: Conectar Projeto ao GitHub

### 4.1 Navegar até a Pasta do Projeto
```bash
cd /home/ubuntu/donshop007
```

### 4.2 Verificar Status do Git
```bash
git status
```

Se aparecer "fatal: not a git repository", execute:
```bash
git init
```

### 4.3 Adicionar Remote Origin
Agora vamos conectar seu projeto local ao repositório do GitHub.

**Cole este comando** (substitua `SEU-USERNAME` pelo seu username do GitHub):

```bash
git remote add origin https://github.com/SEU-USERNAME/donshop007-ecommerce.git
```

**Exemplo real:**
```bash
git remote add origin https://github.com/joaosilva/donshop007-ecommerce.git
```

### 4.4 Verificar Remote
```bash
git remote -v
```

Você deve ver algo como:
```
origin  https://github.com/SEU-USERNAME/donshop007-ecommerce.git (fetch)
origin  https://github.com/SEU-USERNAME/donshop007-ecommerce.git (push)
```

✅ Perfeito! Conexão estabelecida.

---

## 🎯 Passo 5: Fazer Commit e Push do Código

### 5.1 Adicionar Todos os Arquivos
```bash
git add .
```

### 5.2 Fazer o Primeiro Commit
```bash
git commit -m "Primeiro commit: E-commerce DonShop007 completo"
```

### 5.3 Renomear Branch para Main (se necessário)
```bash
git branch -M main
```

### 5.4 Enviar Código para o GitHub (PUSH)
```bash
git push -u origin main
```

**O que vai acontecer:**
- O Git vai pedir suas credenciais do GitHub
- Digite seu **username**
- Digite sua **senha** (ou token de acesso pessoal)

> **⚠️ IMPORTANTE**: Se der erro de autenticação, você precisa criar um **Personal Access Token**:
> 1. Vá em: https://github.com/settings/tokens
> 2. Clique em "Generate new token" → "Generate new token (classic)"
> 3. Dê um nome (ex: "DonShop Deploy")
> 4. Marque a opção **"repo"** (todas as sub-opções)
> 5. Clique em "Generate token"
> 6. **COPIE O TOKEN** (você não verá ele novamente!)
> 7. Use o token como senha no comando `git push`

### 5.5 Aguardar Upload
O Git vai enviar todos os arquivos. Pode levar alguns minutos dependendo da sua internet.

Quando terminar, você verá:
```
Branch 'main' set up to track remote branch 'main' from 'origin'.
```

✅ **SUCESSO!** Código enviado para o GitHub!

---

## 🎯 Passo 6: Verificar se Funcionou

### 6.1 Atualizar Página do GitHub
1. Volte para a página do seu repositório no navegador
2. Pressione **F5** para atualizar
3. Você deve ver todos os arquivos do projeto listados!

### 6.2 Verificar se Está Público
1. Na página do repositório, procure por um badge escrito **"Public"**
2. Se estiver escrito **"Private"**, clique em:
   - **Settings** (Configurações)
   - Role até o final da página
   - Seção **"Danger Zone"**
   - Clique em **"Change visibility"**
   - Selecione **"Make public"**
   - Confirme digitando o nome do repositório

### 6.3 Anotar URL do Repositório
Copie a URL completa do seu repositório:
```
https://github.com/SEU-USERNAME/donshop007-ecommerce
```

**Guarde essa URL!** Você vai precisar dela no deploy do Render.

---

## 🎯 Comandos Resumidos (Para Futuras Atualizações)

Depois que o repositório estiver configurado, para enviar novas alterações:

```bash
# 1. Navegar até a pasta
cd /home/ubuntu/donshop007

# 2. Adicionar alterações
git add .

# 3. Fazer commit
git commit -m "Descrição das alterações"

# 4. Enviar para GitHub
git push origin main
```

---

## ❓ Problemas Comuns e Soluções

### Erro: "Permission denied (publickey)"
**Solução**: Use HTTPS em vez de SSH. Certifique-se de que a URL do remote é:
```bash
git remote set-url origin https://github.com/SEU-USERNAME/donshop007-ecommerce.git
```

### Erro: "Authentication failed"
**Solução**: Crie um Personal Access Token (veja Passo 5.4)

### Erro: "fatal: not a git repository"
**Solução**: Execute `git init` na pasta do projeto

### Erro: "Updates were rejected"
**Solução**: Execute `git pull origin main --rebase` e depois `git push origin main`

---

## ✅ Checklist Final

Antes de prosseguir para o deploy no Render, confirme:

- [ ] Conta no GitHub criada e verificada
- [ ] Repositório `donshop007-ecommerce` criado
- [ ] Repositório está **PUBLIC** (público)
- [ ] Git configurado com seu nome e email
- [ ] Código enviado com sucesso (`git push`)
- [ ] Todos os arquivos visíveis no GitHub
- [ ] URL do repositório anotada

---

## 🎉 Parabéns!

Seu código está agora no GitHub! 🚀

**Próximo passo**: Abra o arquivo `GUIA_RENDER.md` para fazer o deploy do site.

---

## 📞 Precisa de Ajuda?

- **Documentação Git**: https://git-scm.com/doc
- **GitHub Docs**: https://docs.github.com
- **Suporte GitHub**: https://support.github.com

---

**Criado para o projeto DonShop007** | E-commerce com Flask + PostgreSQL
