/**
 * DonShop007 - JavaScript Principal
 */

// Funções de utilidade
const utils = {
    // Formatar preço para BRL
    formatPrice: (price) => {
        return new Intl.NumberFormat('pt-BR', {
            style: 'currency',
            currency: 'BRL'
        }).format(price);
    },

    // Validar CEP
    validateCEP: (cep) => {
        const cepPattern = /^[0-9]{5}-?[0-9]{3}$/;
        return cepPattern.test(cep);
    },

    // Validar email
    validateEmail: (email) => {
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailPattern.test(email);
    },

    // Mostrar loading
    showLoading: (element) => {
        element.disabled = true;
        element.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Carregando...';
    },

    // Esconder loading
    hideLoading: (element, originalText) => {
        element.disabled = false;
        element.innerHTML = originalText;
    }
};

// Consulta de CEP
document.addEventListener('DOMContentLoaded', function() {
    const cepInput = document.getElementById('cep');
    
    if (cepInput) {
        cepInput.addEventListener('blur', function() {
            let cep = this.value.replace(/\D/g, '');
            
            if (cep.length === 8) {
                consultarCEP(cep);
            }
        });
        
        // Máscara de CEP
        cepInput.addEventListener('input', function(e) {
            let value = e.target.value.replace(/\D/g, '');
            
            if (value.length > 5) {
                value = value.replace(/^(\d{5})(\d)/, '$1-$2');
            }
            
            e.target.value = value;
        });
    }
});

async function consultarCEP(cep) {
    const enderecoInput = document.getElementById('endereco');
    const bairroInput = document.getElementById('bairro');
    const cidadeInput = document.getElementById('cidade');
    const estadoInput = document.getElementById('estado');
    const freteDisplay = document.getElementById('frete-valor');
    
    try {
        const response = await fetch(`/pedidos/consultar-cep/${cep}`);
        
        if (!response.ok) {
            throw new Error('CEP não encontrado');
        }
        
        const data = await response.json();
        
        // Preencher campos
        if (enderecoInput && data.endereco) enderecoInput.value = data.endereco;
        if (bairroInput && data.bairro) bairroInput.value = data.bairro;
        if (cidadeInput && data.cidade) cidadeInput.value = data.cidade;
        if (estadoInput && data.estado) estadoInput.value = data.estado;
        
        // Atualizar frete
        if (freteDisplay && data.frete) {
            freteDisplay.textContent = utils.formatPrice(data.frete);
            atualizarTotalComFrete(data.frete);
        }
        
    } catch (error) {
        alert('CEP inválido ou não encontrado. Por favor, verifique.');
        console.error('Erro ao consultar CEP:', error);
    }
}

function atualizarTotalComFrete(frete) {
    const totalElement = document.getElementById('total-pedido');
    const subtotalElement = document.getElementById('subtotal-pedido');
    
    if (totalElement && subtotalElement) {
        const subtotal = parseFloat(subtotalElement.dataset.value);
        const total = subtotal + frete;
        totalElement.textContent = utils.formatPrice(total);
    }
}

// Validação de formulários
document.addEventListener('DOMContentLoaded', function() {
    // Validação de login
    const loginForm = document.getElementById('loginForm');
    if (loginForm) {
        loginForm.addEventListener('submit', function(e) {
            const email = document.getElementById('email').value;
            const senha = document.getElementById('senha').value;
            
            if (!utils.validateEmail(email)) {
                e.preventDefault();
                alert('Por favor, insira um email válido.');
                return false;
            }
            
            if (senha.length < 6) {
                e.preventDefault();
                alert('A senha deve ter pelo menos 6 caracteres.');
                return false;
            }
        });
    }
    
    // Validação de cadastro
    const cadastroForm = document.getElementById('cadastroForm');
    if (cadastroForm) {
        cadastroForm.addEventListener('submit', function(e) {
            const nome = document.getElementById('nome').value;
            const email = document.getElementById('email').value;
            const senha = document.getElementById('senha').value;
            const confirmarSenha = document.getElementById('confirmar_senha').value;
            
            if (nome.length < 3) {
                e.preventDefault();
                alert('Nome deve ter pelo menos 3 caracteres.');
                return false;
            }
            
            if (!utils.validateEmail(email)) {
                e.preventDefault();
                alert('Por favor, insira um email válido.');
                return false;
            }
            
            if (senha.length < 6) {
                e.preventDefault();
                alert('A senha deve ter pelo menos 6 caracteres.');
                return false;
            }
            
            if (senha !== confirmarSenha) {
                e.preventDefault();
                alert('As senhas não coincidem.');
                return false;
            }
        });
    }
});

// Atualizar quantidade no carrinho
function atualizarQuantidade(itemId, novaQuantidade) {
    const form = document.getElementById(`update-form-${itemId}`);
    const input = form.querySelector('input[name="quantidade"]');
    input.value = novaQuantidade;
    form.submit();
}

// Confirmar exclusão
function confirmarExclusao(mensagem) {
    return confirm(mensagem || 'Tem certeza que deseja excluir?');
}

// Avaliação com estrelas
document.addEventListener('DOMContentLoaded', function() {
    const starInputs = document.querySelectorAll('.star-rating input[type="radio"]');
    
    starInputs.forEach(input => {
        input.addEventListener('change', function() {
            const rating = this.value;
            updateStarDisplay(rating);
        });
    });
    
    // Hover effect
    const starLabels = document.querySelectorAll('.star-rating label');
    starLabels.forEach((label, index) => {
        label.addEventListener('mouseenter', function() {
            const rating = starLabels.length - index;
            updateStarDisplay(rating, true);
        });
    });
    
    const starContainer = document.querySelector('.star-rating');
    if (starContainer) {
        starContainer.addEventListener('mouseleave', function() {
            const checkedInput = this.querySelector('input:checked');
            const rating = checkedInput ? checkedInput.value : 0;
            updateStarDisplay(rating, false);
        });
    }
});

function updateStarDisplay(rating, isHover = false) {
    const stars = document.querySelectorAll('.star-rating i');
    stars.forEach((star, index) => {
        const starRating = stars.length - index;
        if (starRating <= rating) {
            star.classList.remove('bi-star');
            star.classList.add('bi-star-fill');
        } else {
            star.classList.remove('bi-star-fill');
            star.classList.add('bi-star');
        }
    });
}

// Preview de imagem de personalização
document.addEventListener('DOMContentLoaded', function() {
    const imageInputs = document.querySelectorAll('input[type="file"][accept*="image"]');
    
    imageInputs.forEach(input => {
        input.addEventListener('change', function(e) {
            const file = e.target.files[0];
            if (file) {
                // Validar tamanho (max 5MB)
                if (file.size > 5 * 1024 * 1024) {
                    alert('A imagem deve ter no máximo 5MB.');
                    this.value = '';
                    return;
                }
                
                // Preview
                const previewId = this.dataset.preview;
                if (previewId) {
                    const preview = document.getElementById(previewId);
                    if (preview) {
                        const reader = new FileReader();
                        reader.onload = function(e) {
                            preview.src = e.target.result;
                            preview.style.display = 'block';
                        };
                        reader.readAsDataURL(file);
                    }
                }
            }
        });
    });
});

// Busca de produtos
document.addEventListener('DOMContentLoaded', function() {
    const searchForm = document.getElementById('searchForm');
    const searchInput = document.getElementById('searchInput');
    
    if (searchForm && searchInput) {
        // Busca ao digitar (debounce)
        let searchTimeout;
        searchInput.addEventListener('input', function() {
            clearTimeout(searchTimeout);
            searchTimeout = setTimeout(() => {
                if (this.value.length >= 3 || this.value.length === 0) {
                    searchForm.submit();
                }
            }, 500);
        });
    }
});

// Smooth scroll para âncoras
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        if (href !== '#' && href !== '#!') {
            e.preventDefault();
            const target = document.querySelector(href);
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        }
    });
});

// Animar elementos ao entrar na viewport
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('fade-in-up');
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

document.addEventListener('DOMContentLoaded', function() {
    const animateElements = document.querySelectorAll('.card, .step-card, .product-card');
    animateElements.forEach(el => observer.observe(el));
});

// Alertas de login social (fake)
document.addEventListener('DOMContentLoaded', function() {
    const socialButtons = document.querySelectorAll('.social-login-btn');
    socialButtons.forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            alert('Login social será implementado em versão futura. Por favor, use login com email e senha.');
        });
    });
});

// Tooltips Bootstrap
document.addEventListener('DOMContentLoaded', function() {
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
});

// Popovers Bootstrap
document.addEventListener('DOMContentLoaded', function() {
    const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });
});
