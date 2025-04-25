from rest_framework.serializers import ModelSerializer

from core.models import Veiculo


class VeiculoSerealizer(ModelSerializer):
    class Meta: 
        model = Veiculo
        field = '__all__'