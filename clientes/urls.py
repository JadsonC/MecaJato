from . import views
from django.urls import path

urlpatterns = [
    path('', views.clientes, name='clientes'),
    path('atualiza_cliente/', views.att_cliente, name='atualiza_cliente')
]