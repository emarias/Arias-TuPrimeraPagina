from django.shortcuts import render, redirect
from sorteo.models import Jugador
import random
from sorteo.forms import FormularioCreacionParticipante

def inicio(request):
    return render(request, 'inicio.html')

def resultados(request):
    jjugadores= Jugador.objects.all()
    
    
    return render(request, 'resultados.html', {'lista_de_jugadores':jjugadores})

def crear_jugador(request):
    formulario = FormularioCreacionParticipante()
    if request.method=="POST":
        formulario = FormularioCreacionParticipante(request.POST)
        if formulario.is_valid():
            nombre = formulario.cleaned_data.get("nombre")
            apellido = formulario.cleaned_data.get("apellido")
            numero_sorteado = random.randint(1,100)
            jjugador = Jugador(nombre=nombre,apellido=apellido,numero_sorteado=numero_sorteado)
            jjugador.save()
            return redirect("resultados")
    return render(request, 'crear_jugador.html',{'formulario':formulario})