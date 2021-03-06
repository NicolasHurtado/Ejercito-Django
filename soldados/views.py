from django.db.models.query_utils import Q
from django.shortcuts import render, redirect


from soldados.models import Arma, Soldado, HistorialSoldado

# Create your views here.

def nuevoSoldado(request):
    
    if request.method == 'POST':
        
        apodo = request.POST.get('apodo').capitalize()
        nombre = request.POST.get('arma')

        print(f"apodo : {apodo}")

        #Se crea el nuevo soldado con los datos ingresados
        arma =  Arma.objects.get(nombre=nombre)
        Soldado(apodo=apodo,arma=arma).save()

        #Se Agrega el registro del historial de arma del soldado
        soldado = Soldado.objects.get(apodo=apodo)
        HistorialSoldado(soldado=soldado,arma=arma).save()

        histo = HistorialSoldado.objects.all()
        sols = Soldado.objects.all()

        print(histo)
        print(sols)

        return redirect('inicio')  # Se vuelve a cargar la pagina de inicio por completo

    armas = Arma.objects.all()
    context = {
        'armas':armas,
    }
    print(armas)    
    return render(request, 'nuevo.html', context)

def gestionarSoldado(request):
    soldados = Soldado.objects.all().order_by('id')
    armas = Arma.objects.all()
    print("asdasdasd ",len(soldados))
    context = {
        'soldados' : soldados,
        'armas' : armas,
    }
    return render(request, 'gestionar.html', context)


def editarSoldado(request, id):
    soldado = Soldado.objects.get(id=id)
    estados = Soldado.estados_choice
    armas = Arma.objects.all()
    
    #Editar una persona en formulario
    if request.method == 'POST':
        armaanterior = soldado.arma.nombre
        arma = request.POST.get('arma')
        nuevaarma =  Arma.objects.get(nombre=arma)
        soldado.apodo = request.POST.get('apodo').capitalize()
        soldado.estado = request.POST.get('estado')
        soldado.arma = nuevaarma
        soldado.save()

        if armaanterior != nuevaarma.nombre:
            HistorialSoldado(soldado=soldado,arma=nuevaarma).save()


        
        return redirect('gestionarSoldado') 

    context = {
        'soldado' : soldado,
        'armas' : armas,
        'estados' : estados,
    }

    return render(request, 'editar.html', context)

def rediGestionar(request):
    return redirect('gestionarSoldado')

def historialSoldado(request, id):
    soldado = Soldado.objects.get(id=id)
    historial = HistorialSoldado.objects.filter(soldado=soldado)

    context = {
        'historial' : historial,
    }
    return render(request, 'historial.html', context)

def nuevasIncorporaciones(request):
    soldados = Soldado.objects.filter(estado="nuevo").order_by('id')
    context = {
        'soldados' : soldados,
    }
    return render(request, 'frentebatalla.html', context)

def frenteBatalla(request):
    soldados = Soldado.objects.filter(estado="frente").order_by('id')
    context = {
        'soldados' : soldados,
    }
    return render(request, 'frentebatalla.html', context)

def heridos(request):
    soldados = Soldado.objects.filter(estado="herido").order_by('id')
    context = {
        'soldados' : soldados,
    }
    return render(request, 'heridos.html', context)

def caidos(request):
    soldados = Soldado.objects.filter(estado="caido").order_by('id')
    context = {
        'soldados' : soldados,
    }
    return render(request, 'heridos.html', context)