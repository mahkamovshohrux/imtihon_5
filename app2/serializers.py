from rest_framework import serializers
from .models import Yangilikmadel1,Yangilikmadel2

class YangilikSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Yangilikmadel1
        fields = ('__all__')

class YangilikSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Yangilikmadel2
        fields = ('__all__')
