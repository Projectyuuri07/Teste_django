from django import forms
from .models import quarto


class FormNome(forms.Form):
    nome = forms.CharField(label='Nome', max_length=20)
    email = forms.EmailField(label='Email', max_length=50)
    senha = forms.CharField(label='Senha',widget=forms.PasswordInput())

class FormCadastro(forms.Form):
    first_name = forms.CharField(label="Nome",max_length=25)
    last_name = forms.CharField(label="Sobrenome",max_length=30)
    user = forms.CharField(label="Usuário", max_length=20)
    email = forms.EmailField(label="Email",max_length=100)
    password = forms.CharField(label="Senha",widget=forms.PasswordInput())

class FormLogin(forms.Form):
    user = forms.CharField(label="Usuário", max_length=20)
    password = forms.CharField(label="Senha",widget=forms.PasswordInput())

class FormReserva(forms.Form):
    user = forms.CharField(label='Usuário', max_length=20)
    email = forms.EmailField(label='Email', max_length=50)
    idade = forms.IntegerField(label='Idade')
    data = forms.DateField(label='Data', widget=forms.DateInput(attrs={'type': 'date'}))
    quarto = forms.ModelChoiceField(label='Quarto', queryset=quarto.objects.filter(id__in=[1, 2, 3, 4, 5]))