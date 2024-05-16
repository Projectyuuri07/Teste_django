from django.shortcuts import render, HttpResponse
from .models import Usuario, hotel, quarto
from .forms import formNome

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


