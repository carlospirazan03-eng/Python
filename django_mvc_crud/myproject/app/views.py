from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

# LISTAR
def index(request):
    productos = Product.objects.all()
    return render(request, 'index.html', {'productos': productos})

# CREAR
def crear(request):
    if request.method == 'POST':
        Product.objects.create(
            nombre=request.POST.get('nombre'),
            descripcion=request.POST.get('descripcion'),
            imagen=request.FILES.get('imagen')
        )
        return redirect('index')
    return render(request, 'form.html')

# EDITAR (UPDATE)
def editar(request, id):
    p = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        p.nombre = request.POST.get('nombre')
        p.descripcion = request.POST.get('descripcion')
        if request.FILES.get('imagen'):
            p.imagen = request.FILES.get('imagen')
        p.save()
        return redirect('index')
    return render(request, 'form.html', {'p': p})

# ELIMINAR
def eliminar(request, id):
    get_object_or_404(Product, id=id).delete()
    return redirect('index')