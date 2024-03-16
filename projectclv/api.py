from .models import DataConsolidado, Cobros, Recaudaciones
from rest_framework import viewsets, permissions
from .serializers import ClvDataSerializer, ClvCobrosSerializer, ClvRecaudacionesSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class DataClvviem(viewsets.ModelViewSet):
    queryset = DataConsolidado.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ClvDataSerializer

    def get_queryset(self):
        codigo_de_pago = self.kwargs.get('codigo_de_pago')
        queryset = DataConsolidado.objects.filter(CODIGO_DE_PAGO=codigo_de_pago)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset)
        serializer = self.serializer_class(obj)
        return Response(serializer.data)

    

class CobrosClvviem(viewsets.ModelViewSet):
    queryset = Cobros.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ClvCobrosSerializer

class RecaudacionClvviem(viewsets.ModelViewSet):
    queryset = Recaudaciones.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ClvRecaudacionesSerializer