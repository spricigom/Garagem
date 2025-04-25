from rest_framework.serializers import ModelSerializer

from core.models import Modelo


class ModeloSerealizer(ModelSerializer):
    class Meta:
        model = Modelo
        fields = '__all__'