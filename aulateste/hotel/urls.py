from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage),
    path('quartos', views.quartos, name='quartos'),
    path('nome', views.nome, name='nome'),
    path('cadastro',views.cadastro, name='cadastro'),
    path('login',views.login, name='login'),
    path('reserva', views.reserva, name='reserva'),
]