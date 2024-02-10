from django.urls import path
from sorteo.views import resultados, inicio, crear_jugador

urlpatterns = [
    path('', inicio, name='inicio'),
    path('resultados/', resultados, name='resultados'),
    path('crear/', crear_jugador, name='crear_jugador'),
]
