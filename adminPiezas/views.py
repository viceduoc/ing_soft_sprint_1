from django.shortcuts import render
from .models import Pieza, Residente
from .forms import  piezaForm
# Create your views here.

def home(request):
    piezas = Pieza.objects.all()
    datos = {
        'piezas': piezas,
    }
    return render(request, 'adminPiezas/home.html', datos)
    

def editForm(request, nro):
    pieza = Pieza.objects.get(nroPieza = nro)

    datos = {
        'form': piezaForm(instance= pieza)

    }

    if request.method == 'POST':
        formulario_edit = piezaForm(data = request.POST, instance= pieza)
        if formulario_edit.is_valid():
            formulario_edit.save()

            datos['mensaje'] = "Pieza modificada con exito"


    return render(request,'adminPiezas/formPieza.html', datos )