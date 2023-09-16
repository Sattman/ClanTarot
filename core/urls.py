from django.urls import path


from .views import (index,
                    contato,
                    produto,
                    cliente,
                    historia, 
                    consulta, 
                    maiores,
                    menores,         
                    carta_paus,
                    carta_copas,
                    carta_espadas, 
                    carta_ouros,
                    arcanos_maiores
                    )

urlpatterns = [
    path('', index, name='Início'),
    path('contato/',contato, name='Contato'),
    path('produto/', produto, name='produto'),
    path('cliente/', cliente, name='cliente'),
    path('historia/', historia, name='História'),
    path('consulta/', consulta, name='Consulta'),
    path('maiores/', maiores, name='Arcanos Maiores'),
    path('menores/', menores, name='Arcanos Menores'),
    path('paus/<str:carta>/', carta_paus, name='carta_paus'),
    path('espadas/<str:carta>/', carta_espadas, name='carta_espadas'),
    path('copas/<str:carta>/', carta_copas, name='carta_copas'),
    path('ouros/<str:carta>/', carta_ouros, name='carta_ouros'),
    path('arcanos_maiores/<str:arcanos>/', arcanos_maiores, name='arcanos_maiores'),
    
]
    

