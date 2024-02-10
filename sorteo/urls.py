from django.urls import path
from sorteo.views import resultados, inicio, crear_jugador

urlpatterns = [
    path('', inicio, name='inicio'),
    path('resultados/', resultados, name='resultados'),
    #path('crear/<str:nombre>/<str:apellido>/<int:numero_sorteado>/', crear_jugador, name='crear_jugador'),
    path('crear/', crear_jugador, name='crear_jugador'),
]
