from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from pdv.models import Pdv

class PdvSerializer(ModelSerializer):
    cnpj = serializers.RegexField(regex='[0-9]{2}\.?[0-9]{3}\.?[0-9]{3}\/?[0-9]{4}\-?[0-9]{2}')
    class Meta:
        model = Pdv
        fields = ['id','tradingName', 'ownerName','cnpj','coverageArea','address']

