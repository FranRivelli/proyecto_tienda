from django.urls import path
from app_tienda import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("about/", views.about, name="about"),
    path("product/", views.product, name="product"),
    path("contact/", views.contact, name="contact"),
    path("contact/contacto", views.contacto, name="contacto"),
    path('zapatillas/', views.zapatillas, name="zapatillas"),
    path('botines/', views.botines, name="botines"),
    path('ropa/', views.ropa, name="ropa"),
    path('otros/', views.otros, name="otros"),
    path('vendedores/', views.vendedores, name="vendedores"),
    path('clientes/', views.clientes, name="clientes"),
    path('zapatillas/formulario/', views.formulario_zapatillas, name="formulario_zapatillas"),
    path('zapatillas/exito/', views.registro_zapatillas, name="registro_zapatillas"),
    path('botines/formulario/', views.formulario_botines, name="formulario_botines"),
    path('botines/exito/', views.registro_botines, name="registro_botines"),
    path('ropa/formulario/', views.formulario_ropa, name="formulario_ropa"),
    path('ropa/exito/', views.registro_ropa, name="registro_ropa"),
    path('otros/formulario/', views.formulario_otros, name="formulario_otros"),
    path('otros/exito/', views.registro_otros, name="registro_otros"),
    path('vendedores/formulario/', views.formulario_vendedores, name="formulario_vendedores"),
    path('vendedores/exito/', views.registro_vendedores, name="registro_vendedores"),
    path('clientes/formulario/', views.formulario_clientes, name="formulario_clientes"),
    path('clientes/exito/', views.registro_clientes, name="registro_clientes"),
]

