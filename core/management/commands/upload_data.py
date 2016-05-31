# coding=utf-8

__author__ = 'wilson'

import json
import os
from django.core.management.base import BaseCommand

from ...models import Pais, Departamento, Provincia, Distrito

data = json.loads(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/departamento_provincia_distrito.json")).read())


class Command(BaseCommand):

    def handle(self, *args, **options):
        # self.conteo()
        print (data)
        pais, created = Pais.objects.get_or_create(nombre="PERÚ", codigo="PE")

        for x in data:
            if x['model'] == "ubigeo.departamento":
                Departamento.objects.create(nombre=x['fields']['nombre'], pais=pais)
            if x['model'] == "ubigeo.provincia":
                Provincia.objects.create(nombre=x['fields']['nombre'], departamento=Departamento.objects.get(id=x['fields']['departamento']))
            elif x['model'] == "ubigeo.distrito":
                Distrito.objects.create(nombre=x['fields']['nombre'], provincia=Provincia.objects.get(id=x['fields']['provincia']))

