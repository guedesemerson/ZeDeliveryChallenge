from django.db import models
from django.contrib.gis.db import models as tipo
from localflavor.br.models import BRCNPJField


class Pdv(models.Model):

    tradingName = models.CharField(max_length=150, blank=False)
    ownerName = models.CharField(max_length=100, blank=False)
    cnpj =  BRCNPJField(blank=False, unique=True)
    coverageArea = tipo.MultiPolygonField(blank=False)
    address = tipo.PointField(blank=False)



    def __str__(self):
        return self.tradingName

