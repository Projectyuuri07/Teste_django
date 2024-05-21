from django import forms

class formNome(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    sobrenome = forms.CharField(label='Sobrenome', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    telefone = forms.CharField(label='Telefone', max_length=100)
    senha = forms.CharField(label='Senha', max_length=20, widget=forms.PasswordInput())

class ForCadastro(forms.Form):
    first_name = forms.CharField(label='Nome', max_length=20)
    last_name = forms.CharField(label='Sobrenome', max_length=20)
    user = forms.CharField(label='Usuario', max_length=20)
    email = forms.EmailField(label='Email', max_length=100)
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)

class forLogin(forms.Form):
    user = forms.CharField(label='Usuario', max_length=20)
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)