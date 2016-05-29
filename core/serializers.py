from .models import Departamento
from .models import Provincia

from rest_framework import serializers


class DepartametnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = ('id', 'nombre')


class ProvinciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provincia
        fields = ('id', 'nombre')