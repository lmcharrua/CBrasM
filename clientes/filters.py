from .models import Clientes
import django_filters

class ClienteFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Clientes
        fields = ['nome', ]
        