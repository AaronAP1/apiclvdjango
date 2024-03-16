from django.shortcuts import render
from  rest_framework import generics, authentication, permissions
from  rest_framework.authtoken.views  import ObtainAuthToken 
from projectclv.serializers import UserSerializer, AuthTokenSerializer
from projectclv.models import User
from django.http import JsonResponse, HttpResponse
from django.db import connection
from django.views import View
from django.template.loader import get_template
from xhtml2pdf import pisa

# Create your views here.


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class RetroviewUpdateUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer


def mi_pagina(request):
    return render(request, 'principal.html')

def recaudaciones(request):
    return render(request, 'recaudaciones.html')

def busqueda(request):
    return render(request, 'listar.html')

class NuevaVistaPrincipal(View):
    def get(self, request):
        # Renderizar el nuevo template deseado
        return render(request, 'listar.html')

def tu_vista(request, codigo_pago):
    with connection.cursor() as cursor:
        # Tu consulta SQL personalizada
        consulta = """
        SELECT
            c."NUMERO_DE_RECIBO" AS c_numero_recibo,
            c."DESCRIPCION_COBRO_REALIZAR" AS c_descripcion,
            c."IMPORTE_COBRO_COMPLETO" AS c_importe,
            c."FECHA_VENCIMIENTO_RECIBO" AS c_fecha_vencimiento,
            c."INDICADOR_COBRO_MORA" AS c_indicador_mora,
            c."OBSERVACIONES_RECIBO" AS c_observaciones
        FROM
            estadosdecuenta_dataconsolidado d
        LEFT JOIN
            estadosdecuenta_cobros c ON d."CODIGO DE PAGO" = c."CODIGO_INTEGRANTE"
        WHERE
            d."CODIGO DE PAGO" = %s;
        """
        cursor.execute(consulta, [codigo_pago])

        # Recuperar los resultados de la consulta
        resultados = cursor.fetchall()

    # Procesar los resultados como desees
    data = [
        {
            'c_numero_recibo': row[0],
            'c_descripcion': row[1],
            'c_importe': row[2],
            'c_fecha_vencimiento': row[3],
            'c_indicador_mora': row[4],
            'c_observaciones': row[5]
        }
        for row in resultados
    ]

    return JsonResponse(data, safe=False)


def recaudacionesbusqueda(request, codigo_pago):
    with connection.cursor() as cursor:
        # Nueva consulta SQL personalizada
        consulta = """
SELECT
    c."NUMERO_DE_RECIBO" AS cobro_numero_recibo,
    c."DESCRIPCION_RECIBO" AS cobro_descripcion_recibo,
    c."IMP_TOTAL" AS cobro_imp_total,
    c."FECHA_VENCIMIENTO" AS cobro_fecha_vencimiento,
    c."FORMA_PAGO" AS cobro_forma_pago
FROM
    estadosdecuenta_dataconsolidado d
LEFT JOIN
    estadosdecuenta_recaudaciones c ON d."CODIGO DE PAGO" = c."CODIGO_INTEGRANTE"
WHERE
    d."CODIGO DE PAGO" = %s;
        """
        cursor.execute(consulta, [codigo_pago])

        # Recuperar los resultados de la consulta
        resultados = cursor.fetchall()

    # Procesar los resultados como desees
    data = [
        {
            'cobro_numero_recibo': row[0],
            'cobro_descripcion': row[1],
            'cobro_importe': row[2],
            'cobro_fecha_vencimiento': row[3],
            'cobro_forma_pago': row[4]
        }
        for row in resultados
    ]

    return JsonResponse(data, safe=False)


class GeneratePDFView(View):
    def get(self, request, *args, **kwargs):
        template = get_template('listar.html')
        context = {'title': 'Descargar Info'}
        html = template.render(context)

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="descarga.pdf"'  

        pisa_status = pisa.CreatePDF(html, dest=response)

        if pisa_status.err:
            return HttpResponse('Errorxdxd')

        return response