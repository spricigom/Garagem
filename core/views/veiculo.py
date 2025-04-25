from rest_framework.viewsets import ModelViewSet

from core.models import Veiculo
from core.serializers import VeiculoSerealizer

class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerealizer
