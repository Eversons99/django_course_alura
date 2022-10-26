from django.shortcuts import render, redirect

# Create your views here.
def cadastro(request):
    if request.method == 'POST':
        print('Usuário criado com sucesso')
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')
     
def login(request):
    return render(request, 'usuarios/login.html')

def logout(request):
    pass

def dashboard(request):
    pass