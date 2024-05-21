from django.shortcuts import render, HttpResponse
from .models import Reserva_quarto, hotel, quarto, Usuario
from .forms import FormNome, FormCadastro, FormLogin, FormReserva
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
    context['dados_quarto'] = dados_quarto
    return render(request, 'quartos.html', context)

def nome(request):
    if request.method == "POST":
        form = FormNome(request.POST)
        if form.is_valid():
            var_nome = form.cleaned_data['nome']
            var_email = form.cleaned_data['email']
            var_senha = form.cleaned_data['senha']

            user = Usuario(nome=var_nome, email=var_email, senha=var_senha)
            user.save()

            return HttpResponse("<h1>thanks</h1>")
    else:
        form = FormNome()

        return render(request, "nome.html", {"form": form})

def cadastro(request):
    if request.method == "POST":
        form = FormCadastro(request.POST)
        if form.is_valid():

            var_first_name = form.cleaned_data['first_name']
            var_last_name = form.cleaned_data['last_name']
            var_user = form.cleaned_data['user']
            var_email = form.cleaned_data['email']
            var_password = form.cleaned_data['password']         

            user = User.objects.create_user(username=var_user,email=var_email,password=var_password)
            user.first_name = var_first_name
            user.last_name = var_last_name
            user.save()

            return HttpResponse("<h1>thanks</h1>")
    else:
        form = FormCadastro()

        return render(request, "cadastro.html", {"form": form})

def login(request):
    if request.method == "POST":
        form = FormLogin(request.POST)
        if form.is_valid():

            var_user = form.cleaned_data['user']
            var_password = form.cleaned_data['password']         

            user = authenticate(username=var_user, password=var_password)
            if user is not None:
                return HttpResponse("<h1>Login realizado</h1>")
            else:
                return HttpResponse("<h1>Usuário ou senha inválida</h1>")
    else:
        form = FormLogin()

        return render(request, "login.html", {"form": form})   

def reserva(request):
    if request.method == "POST":
        form = FormReserva(request.POST)
        if form.is_valid():
            var_nome = form.cleaned_data['nome']
            var_email = form.cleaned_data['email']
            var_idade = form.cleaned_data['idade']
            var_data = form.cleaned_data['data']
            var_quarto = form.cleaned_data['quarto']

            reservar_quarto = Reserva_quarto(nome=var_nome, email=var_email, idade=var_idade, data=var_data, quarto=var_quarto)
            reservar_quarto.save()

            return render(request, "reserva.html")
    else:
        form = FormReserva()
        
    return render(request, "reserva.html", {"form": form})