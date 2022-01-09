from django.shortcuts import render

# Create your views here.

""" def detallePersona(request, id):
    # persona = Persona.objects.get(pk=id)
    persona = get_object_or_404(Persona, pk=id)  # Si no encuentra un pk, te dirije a la pag 404 error
    return render(request, 'personas/detalle.html', {'persona': persona})


#PersonaForm = modelform_factory(Persona, exclude=[])

def nuevaPersona(request):
    #Agregar una nueva persona en formulario
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST) #Llenar nuevo objeto
        if formaPersona.is_valid():
            formaPersona.save() #Guarda la informacion insertada en la base de datos
            return redirect('inicio')  # Se vuelve a cargar la pagina de inicio por completo
    else:
        formaPersona = PersonaForm()

    return render(request, 'personas/nuevo.html', {'formaPersona': formaPersona})

def editarPersona(request, id):
    persona = get_object_or_404(Persona, pk=id)  # Si no encuentra un pk, te dirije a la pag 404 error
    #Editar una persona en formulario
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST, instance=persona) #Llenar nuevo objeto
        if formaPersona.is_valid():
            formaPersona.save() #Guarda la informacion insertada en la base de datos
            return redirect('inicio')  # Se vuelve a cargar la pagina de inicio por completo
    else:
        formaPersona = PersonaForm(instance=persona)

    return render(request, 'personas/editar.html', {'formaPersona': formaPersona})

def eliminarPersona(request, id):
    persona = get_object_or_404(Persona, pk=id)  # Si no encuentra un pk, te dirije a la pag 404 error
    #Eliminar una persona en formulario
    if persona:
        persona.delete()
    return redirect('inicio')

def detalleDomicilio(request, id):
    domicilio = get_object_or_404(Domicilio, pk=id)  # Si no encuentra un pk te dirije a la pag 404 error
    return render(request, 'domicilios/detalle.html', {'domicilio': domicilio})

def nuevoDomicilio(request):
    #Agregar una nueva persona en formulario
    if request.method == 'POST':
        formaDomicilio = DomicilioForm(request.POST) #Llenar nuevo objeto
        if formaDomicilio.is_valid():
            formaDomicilio.save() #Guarda la informacion insertada en la base de datos
            return redirect('domicilios')  # Se vuelve a cargar la pagina de inicio por completo
    else:
        formaDomicilio = DomicilioForm()

    return render(request, 'domicilios/nuevo.html', {'formaDomicilio': formaDomicilio})

def editarDomicilio(request, id):
    domicilio = get_object_or_404(Domicilio, pk=id)  # Si no encuentra un pk, te dirije a la pag 404 error
    #Editar un domicilio en formulario
    if request.method == 'POST':
        formaDomicilio = DomicilioForm(request.POST, instance=domicilio) #Llenar nuevo objeto
        if formaDomicilio.is_valid():
            formaDomicilio.save() #Guarda la informacion insertada en la base de datos
            return redirect('domicilios')  # Se vuelve a cargar la pagina de inicio por completo
    else:
        formaDomicilio = DomicilioForm(instance=domicilio)

    return render(request, 'domicilios/editar.html', {'formaDomicilio': formaDomicilio})

def eliminarDomicilio(request, id):
    domicilio = get_object_or_404(Domicilio, pk=id)  # Si no encuentra un pk, te dirije a la pag 404 error
    #Eliminar una persona en formulario
    if domicilio:
        domicilio.delete()
    return redirect('domicilios') """