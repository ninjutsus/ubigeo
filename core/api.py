import json

from .models import Departamento
from .models import Provincia

from .serializers import DepartametnoSerializer
from .serializers import ProvinciaSerializer
from .serializers import DistritoSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET', ])
def api_departamentos(request):
    departamentos = Departamento.objects.all()
    serializer = DepartametnoSerializer(departamentos, many=True)
    return Response(serializer.data)

@api_view(['GET', ])
def api_provincias(request, pk):
    """
    pk: pk de departamento
    """
    departamento = Departamento.objects.get(pk=pk)
    provincias = departamento.provincias.all()
    serializer = ProvinciaSerializer(provincias, many=True)
    return Response(serializer.data)

@api_view(['GET', ])
def api_distritos(request, pk):
    """
    pk: pk de provincia
    """
    provincia = Provincia.objects.get(pk=pk)
    distritos = provincia.distritos.all()
    serializer = DistritoSerializer(distritos, many=True)
    return Response(serializer.data)

