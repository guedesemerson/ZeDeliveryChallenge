from django.contrib.gis.db.models.functions import Distance
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from django.contrib.gis.geos import GEOSGeometry
from pdv.models import Pdv
from .serializers import PdvSerializer
class PdvViewSet(ModelViewSet):

    queryset = Pdv.objects.all()
    serializer_class = PdvSerializer
    filter_backends = (SearchFilter,)
    search_fields = ['address',]

    def get_queryset(self):
        busca = super().get_queryset()
        latitude = self.request.query_params.get('lat', None)
        longitude = self.request.query_params.get('lng', None)

        if latitude and longitude:
            pnt= GEOSGeometry('POINT(' +str(longitude)+' '+ str(latitude) + ')',srid=4326)
            busca= busca.annotate(distance =Distance('coverageArea',pnt)).order_by('coverageArea')
        return busca

