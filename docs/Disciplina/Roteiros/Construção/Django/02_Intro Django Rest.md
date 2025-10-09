# Introdução ao Django REST

Uma extensão do aplicativo Django inicial para incluir uma API RESTful usando Django REST Framework, mantendo a funcionalidade existente e adicionando endpoints API.

## 1. Instalação e Configuração Inicial

Primeiro, vamos instalar e configurar o DRF:

```bash
pip install djangorestframework
```

Adicione ao `INSTALLED_APPS` em `myproject/settings.py`:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'myapp',
]
```

## 2. Criação dos Serializers

Crie um arquivo `serializers.py` na aplicação `minhaapp`:

```python
# minhaapp/serializers.py
from rest_framework import serializers
from myapp.models import Produto

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'nome', 'preco', 'descricao', 'disponivel']
        read_only_fields = ['id']
```

## 3. Criação das Viewsets e API Views

Atualize ou crie um arquivo `api.py` na aplicação:

```python
# minhaapp/api.py
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from myapp.models import Produto
from myapp.serializers import ProdutoSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    

## 4. Configuração das URLs da API

Crie um arquivo `api_urls.py` na aplicação:

```python
# myapp/api_urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from minhaapp.api import ProdutoViewSet

router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet, basename='produto')

urlpatterns = [
    path('', include(router.urls)),
]
```

Atualize o `urls.py` principal do projeto:

```python
# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('minhaapp.api_urls')),  # URLs da API
]
```

## 5. Testando a API

Agora você pode testar os endpoints da API:

1. **Listar todos os produtos**: `GET /api/produtos/`
2. **Criar novo produto**: `POST /api/produtos/`
3. **Detalhes de um produto**: `GET /api/produtos/1/`
4. **Atualizar produto**: `PUT /api/produtos/1/`

Esta extensão transforma seu aplicativo Django em uma API RESTful poderosa enquanto mantém a funcionalidade web tradicional. Você agora pode:

- Consumir a API com frontends modernos (React, Vue, Angular)
- Oferecer serviços para aplicativos móveis
- Integrar com outros sistemas via API
- Manter uma arquitetura escalável e bem organizada
