from django.shortcuts import render, HttpResponse
from .models import Usuario, hotel, quarto
from .forms import ForCadastro, formNome, forLogin
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.

def homepage(request):
    context = {}
    dados_hotel = hotel.objects.all()
    context["dados_hotel"] = dados_hotel
    return render(request, 'homepage.html', context)

def quartos(request):
    context = {}
    dados_quarto = quarto.objects.all()
    context["dados_quarto"] = dados_quarto
    return render(request, 'quartos.html', context)

def nome(request):
    if request.method == "POST":
        form = formNome(request.POST)
        if form.is_valid():
            var_nome = form.cleaned_data["nome"]
            var_sobrenome = form.cleaned_data["sobrenome"]
            var_email = form.cleaned_data["email"]
            var_telefone = form.cleaned_data["telefone"]
            var_senha = form.cleaned_data["senha"]

            return HttpResponse("<h1>Deu Certo</h1>")
        
        user = Usuario(nome=var_nome, sobrenome=var_sobrenome, email=var_email, telefone=var_telefone, senha=var_senha)
        user.save()

        print(var_nome)
        print(var_sobrenome)
        print(var_email)
        print(var_telefone)
        print(var_senha)

    else:
        form = formNome()


    return render(request, "nome.html", {"form": form})


def cadastro(request):
    if request.method == "POST":
        form = ForCadastro(request.POST)
        if form.is_valid():
            var_Firstname = form.cleaned_data["first_name"]
            var_Lastname = form.cleaned_data["last_name"]
            var_user = form.cleaned_data["user"]
            var_email = form.cleaned_data["email"]
            var_password = form.cleaned_data["password"]

            return HttpResponse("<h1>Deu Certo</h1>")
        
        user = User.objects.create_user(username=var_user, email=var_email, password=var_password)
        user.first_name = var_Firstname
        user.last_name = var_Lastname
        user.save()

        print(var_Firstname)
        print(var_Lastname)
        print(var_user)
        print(var_email)
        print(var_password)

    else:
        form = ForCadastro()


    return render(request, "cadastro.html", {"form": form})

def login(request):
    if request.method == "POST":
        form = forLogin(request.POST)
        if form.is_valid():
            var_user = form.cleaned_data["user"]
            var_password = form.cleaned_data["password"]

            return HttpResponse("<h1>Deu Certo</h1>")
        
        print(var_user)
        print(var_password)

        user = authenticate(username=var_user, password=var_password)
        if user is not None:
            return HttpResponse("<h1>Logado com sucesso</h1>")
        else:
            return HttpResponse("<h1>Usuario ou senha invalidos</h1>")
        

    else:
        form = forLogin()


    return render(request, "login.html", {"form": form})

