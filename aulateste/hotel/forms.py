from django import forms

class formNome(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    sobrenome = forms.CharField(label='Sobrenome', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    telefone = forms.CharField(label='Telefone', max_length=100)