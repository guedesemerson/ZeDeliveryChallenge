from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from pdv.models import Pdv
from .serializers import PdvSerializer
class PdvViewSet(ModelViewSet):

    queryset = Pdv.objects.all()
    serializer_class = PdvSerializer
    filter_backends = (SearchFilter,)
    search_fields = ['address',]
