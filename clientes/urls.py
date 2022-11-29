from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from clientes.views import ClienteDetalhe, TratamentoLista
from .views import (
    Clientes_Lista,
    Clientes_criar,
    ClienteUpdate,
    Tratamento_criar,
    TratamentoUpdate,
    Exame_criar,
    Exame_view,
    ExameUpdate,
  

)

app_name = "clientes"

urlpatterns = [
    path('', Clientes_Lista.as_view(), name='clientes-lista'),
    
    #Links de gestão de clientes
    
    path('create/', Clientes_criar.as_view(), name='clientes-create'),
    path('cliente/<int:pk>', ClienteDetalhe, name='clientes-detail'),
    path('cliente/update/<int:pk>', ClienteUpdate.as_view(), name = 'clientes-update'),
    path('tratamento/<int:pk>', TratamentoLista, name = 'tratamentos-lista'),
    path('tratamento/update/<int:pk>', TratamentoUpdate.as_view(), name = 'tratamento-update'),
    path('criar/<int:pk>', Tratamento_criar.as_view(), name = 'tratamento-create'),
    path('exame/<int:pk>', Exame_criar.as_view(), name = 'exame-create'),
    path('exames/view/<str:pk>', Exame_view, name = 'exame-view'),
    path('exame/update/<int:pk>', ExameUpdate.as_view(), name = 'exame-update'),
    # path('search/', search, name='search'),
    # Links de gestão de Tratamentos

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)