from django.shortcuts import render, redirect, get_object_or_404
# Conexão com a table user do banco 
from django.contrib.auth.models import User
from django.contrib import auth, messages
from receitas.models import Receita

# Create your views here.
def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        
        # Validando se o campo esta em branco, se sim o usuário será redirecionado novamente para a página de cadastro
        if campo_vazio(nome):
            messages.error(request, 'O campo nome não pode ficar em branco')
            return redirect('cadastro')

        if campo_vazio(email):
            messages.error(request, 'O campo email não pode ficar branco')
            return redirect('cadastro')

        if senhas_nao_sao_iguais(senha, senha2):
            messages.error(request, 'As senhas não são iguais')
            return redirect('cadastro')
        
        # Verificando se email do usuário já existe no banco 
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Usuário já cadastrado')
            return redirect('cadastro')
        
        # Verificando se o usuário já existe no banco 
        if User.objects.filter(username=nome).exists():
            messages.error(request, 'Usuário já cadastrado')
            return redirect('cadastro')

        # Criando usuário no BDq
        user = User.objects.create_user(username=nome, email=email, password=senha)
        # Inserindo usuário no BD
        user.save()
        messages.success(request, 'Usuário cadastrado com sucesso')
        return redirect('login')

    else:
        return render(request, 'usuarios/cadastro.html')
     
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']

        if campo_vazio(email) or campo_vazio(senha):
            messages.warning(request, 'Os campos senha e email não podem ficar em branco')
            return redirect('login')

        if User.objects.filter(email=email).exists():
            # Buscando o usarname, que quando retornado fica na posição 0
            nome = User.objects.filter(email=email).values_list('username', flat=True)[0]
            # Autenticando o usuário no sistema
            user = auth.authenticate(request, username=nome, password=senha) 

            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')

    return render(request, 'usuarios/login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def dashboard(request):
    if request.user.is_authenticated:
        id = request.user.id # Pegando usuario que fez a requisição (pegando o ID)
        # Buscando todas receitas no banco mas filtrando as que possuem o ID igual ao user que esta logado
        receitas = Receita.objects.order_by('-data_receita').filter(pessoas=id)

        dados = {
            'receitas' : receitas
        }

        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('index')

def cria_receita(request):
    if request.method == 'POST':
        nome_receita = request.POST['nome_receita']
        ingredientes = request.POST['ingredientes']
        modo_preparo = request.POST['modo_preparo']
        tempo_preparo = request.POST['tempo_preparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        foto_receita = request.FILES['foto_receita']
        user = get_object_or_404(User, pk=request.user.id) # Pegando usuario que fez a requisição
        # Criando meu objeto receita
        receita = Receita.objects.create(
            pessoas=user, 
            nome_receita=nome_receita, 
            ingredientes=ingredientes, 
            modo_preparo=modo_preparo, 
            tempo_preparo=tempo_preparo, 
            rendimento=rendimento, 
            categoria=categoria, 
            foto_receita=foto_receita
        )
        # Salvando meu objeto no banco 
        receita.save()

        return redirect('dashboard')
    else:
        return render(request, 'usuarios/cria_receita.html')

def campo_vazio(campo):
    return not campo.strip()

def senhas_nao_sao_iguais(senha, senha2):
    return senha != senha2
