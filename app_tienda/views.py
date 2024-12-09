from django.shortcuts import render, redirect
from .models import *
from django.core.files.storage import FileSystemStorage

# Create your views here.
def inicio(request):
    return render(request, "app_tienda/index.html")

def about(request):
    return render(request, "app_tienda/about.html")

def product(request):
    return render(request, "app_tienda/product.html")

def contact(request):
    return render(request, "app_tienda/contact.html")

def zapatillas(request):
    query = request.GET.get('q')
    if query:
        zapatillas = Zapatillas.objects.filter(modelo__icontains=query)
    else:
        zapatillas = Zapatillas.objects.all()
    return render(request, "app_tienda/zapatillas.html", {"zapatillas":zapatillas, "query":query})

def botines(request):
    query = request.GET.get('q')
    if query:
        botines = Botines.objects.filter(modelo__icontains=query)
    else:
        botines = Botines.objects.all()
    return render(request, "app_tienda/botines.html", {"botines":botines, "query":query})

def ropa(request):
    query = request.GET.get('q')
    if query:
        ropa = Ropa.objects.filter(modelo__icontains=query)
    else:
        ropa = Ropa.objects.all()
    return render(request, "app_tienda/ropa.html", {"ropa":ropa, "query":query})

def otros(request):
    query = request.GET.get('q')
    if query:
        otros = Otros_Productos.objects.filter(producto__icontains=query)
    else:
        otros = Otros_Productos.objects.all()
    return render(request, "app_tienda/otros.html", {"otros":otros, "query":query})

def vendedores(request):
    query = request.GET.get('q')
    if query:
        vendedores = Vendedores.objects.filter(apellido__icontains=query)
    else:
        vendedores = Vendedores.objects.all()
    return render(request, "app_tienda/vendedores.html", {"vendedores":vendedores, "query":query})

def clientes(request):
    query = request.GET.get('q')
    if query:
        clientes = Clientes.objects.filter(apellido__icontains=query)
    else:
        clientes = Clientes.objects.all()
    return render(request, "app_tienda/clientes.html", {"clientes":clientes, "query":query})

def formulario_zapatillas(request):
    if request.method == "POST":
        modelo = request.POST.get("modelo")
        precio = request.POST.get("precio")
        talle_arg = request.POST.get("talle_arg")
        vendedor = request.POST.get("vendedor")
        descripcion = request.POST.get("descripcion")
        imagen = request.FILES.get("imagen")
        zapatillas = Zapatillas(
            modelo=modelo,
            precio=precio,
            talle_arg=talle_arg,
            vendedor=vendedor,
            descripcion=descripcion,
            imagen=imagen,
        )
        zapatillas.save()
        return redirect('registro_zapatillas')
    return render(request, "app_tienda/forms/zapatillas_formularios.html")

def registro_zapatillas(request):
    return render(request, "app_tienda/forms/registro_zapatillas.html")

def formulario_botines(request):
    if request.method == "POST":
        modelo = request.POST.get("modelo")
        precio = request.POST.get("precio")
        talle_arg = request.POST.get("talle_arg")
        vendedor = request.POST.get("vendedor")
        descripcion = request.POST.get("descripcion")
        imagen = request.FILES.get("imagen")
        botines = Botines(
            modelo=modelo,
            precio=precio,
            talle_arg=talle_arg,
            vendedor=vendedor,
            descripcion=descripcion,
            imagen=imagen,
        )
        botines.save()
        return redirect('registro_botines')
    return render(request, "app_tienda/forms/botines_formularios.html")

def registro_botines(request):
    return render(request, "app_tienda/forms/registro_botines.html")

def formulario_ropa(request):
    if request.method == "POST":
        modelo = request.POST.get("modelo")
        precio = request.POST.get("precio")
        talle_arg = request.POST.get("talle_arg")
        vendedor = request.POST.get("vendedor")
        descripcion = request.POST.get("descripcion")
        imagen = request.FILES.get("imagen")
        ropa = Ropa(
            modelo=modelo,
            precio=precio,
            talle_arg=talle_arg,
            vendedor=vendedor,
            descripcion=descripcion,
            imagen=imagen,
        )
        ropa.save()
        return redirect('registro_ropa')
    return render(request, "app_tienda/forms/ropa_formularios.html")

def registro_ropa(request):
    return render(request, "app_tienda/forms/registro_ropa.html")

def formulario_otros(request):
    if request.method == "POST":
        producto = request.POST.get("modelo")
        precio = request.POST.get("precio")
        vendedor = request.POST.get("vendedor")
        descripcion = request.POST.get("descripcion")
        imagen = request.FILES.get("imagen")
        otros = Otros_Productos(
            producto=producto,
            precio=precio,
            vendedor=vendedor,
            descripcion=descripcion,
            imagen=imagen,
        )
        otros.save()
        return redirect('registro_otros')
    return render(request, "app_tienda/forms/otros_formularios.html")

def registro_otros(request):
    return render(request, "app_tienda/forms/registro_otros.html")

def formulario_vendedores(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        email = request.POST.get("email")
        telefono = request.POST.get("telefono")
        vendedores = Vendedores(
            nombre=nombre,
            apellido=apellido,
            email=email,
            telefono=telefono
        )
        vendedores.save()
        return redirect('registro_vendedores')
    return render(request, "app_tienda/forms/vendedores_formularios.html")

def registro_vendedores(request):
    return render(request, "app_tienda/forms/registro_vendedores.html")

def formulario_clientes(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        email = request.POST.get("email")
        telefono = request.POST.get("telefono")
        clientes = Clientes(
            nombre=nombre,
            apellido=apellido,
            email=email,
            telefono=telefono
        )
        clientes.save()
        return redirect('registro_clientes')
    return render(request, "app_tienda/forms/clientes_formularios.html")

def registro_clientes(request):
    return render(request, "app_tienda/forms/registro_clientes.html")

def contacto(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        email = request.POST.get("email")
        telefono = request.POST.get("telefono")
        descripcion = request.POST.get("descripcion")
        contacto = Contacto(
            nombre=nombre,
            email=email,
            telefono=telefono,
            descripcion=descripcion
        )
        contacto.save()
        return redirect('contact')
    return render(request, "app_tienda/contact.html")