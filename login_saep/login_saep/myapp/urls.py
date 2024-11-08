from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.listar_usuarios, name='listar_usuarios'),
    path('adicionar/', views.criar_usuarios, name='criar_usuarios'),
   path('deletar/<int:id>/', views.deletar_usuarios, name='deletar_usuarios'),
    path('atualizar/<int:id>/', views.atualizar_usuarios, name='atualizar_usuarios'),
    
]