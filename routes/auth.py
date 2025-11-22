
"""
Rotas de autenticação (login, cadastro, logout)
"""
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from models import db, User, Cart

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Página de login"""
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        lembrar = request.form.get('lembrar') == 'on'
        
        user = User.query.filter_by(email=email).first()
        
        if user and user.check_password(senha):
            login_user(user, remember=lembrar)
            
            # Redirecionar para a página que o usuário tentou acessar
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('main.index'))
        else:
            flash('Email ou senha incorretos.', 'danger')
    
    return render_template('auth/login.html')


@auth_bp.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    """Página de cadastro"""
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        confirmar_senha = request.form.get('confirmar_senha')
        
        # Validações
        if not nome or not email or not senha:
            flash('Todos os campos são obrigatórios.', 'danger')
            return render_template('auth/cadastro.html')
        
        if senha != confirmar_senha:
            flash('As senhas não coincidem.', 'danger')
            return render_template('auth/cadastro.html')
        
        if len(senha) < 6:
            flash('A senha deve ter pelo menos 6 caracteres.', 'danger')
            return render_template('auth/cadastro.html')
        
        # Verificar se o email já existe
        if User.query.filter_by(email=email).first():
            flash('Este email já está cadastrado.', 'danger')
            return render_template('auth/cadastro.html')
        
        # Criar novo usuário
        user = User(nome=nome, email=email)
        user.set_password(senha)
        
        db.session.add(user)
        db.session.commit()
        
        # Criar carrinho para o usuário
        cart = Cart(user_id=user.id)
        db.session.add(cart)
        db.session.commit()
        
        flash('Cadastro realizado com sucesso! Faça login para continuar.', 'success')
        return redirect(url_for('auth.login'))
    
    return render_template('auth/cadastro.html')


@auth_bp.route('/logout')
@login_required
def logout():
    """Logout do usuário"""
    logout_user()
    flash('Você saiu da sua conta.', 'info')
    return redirect(url_for('main.index'))
