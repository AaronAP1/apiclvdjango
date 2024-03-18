from rest_framework import routers
from django.urls import path, include
from projectclv import views
from .api import DataClvviem, CobrosClvviem, RecaudacionClvviem
from .views import mi_pagina, recaudaciones, tu_vista, busqueda, recaudacionesbusqueda, GeneratePDFView, NuevaVistaPrincipal, UserLoginAPIView
from django.urls import path, include

router = routers.DefaultRouter()

router.register('api/clvdat/(?P<codigo_de_pago>\w+)', DataClvviem, 'DataConsolidada')
router.register('api/clvco/(?P<codigo_integrante>\w+)', CobrosClvviem, 'Cobros')
router.register('api/clvrec/(?P<codigo_integrante>\w+)', RecaudacionClvviem, 'Recaudaciones')


urlpatterns = [
    path('crear/',views.CreateUserView.as_view()),
    path('token/',views.CreateTokenView.as_view()),
    path('usuario/',views.RetroviewUpdateUserView.as_view()),
    path('login/', UserLoginAPIView.as_view(), name='user-login'),
    path('', mi_pagina, name='mi_pagina'),
     path('nueva/', NuevaVistaPrincipal.as_view(), name='nueva_vista_principal'),
    path('listarb/', busqueda, name='listar'),
    path('recaudaciones/', recaudaciones, name='recaudaciones'),
    path('consultacobros/<str:codigo_pago>/', tu_vista, name='nombre_de_la_vista'),
    path('consultarecau/<str:codigo_pago>/', recaudacionesbusqueda, name='nombre_de_la_vista'),
    path('descargar/', GeneratePDFView.as_view(), name='descargar'),
    # Agrega esta línea para tu página personalizada
    path('consumo/', include(router.urls)),
    
]