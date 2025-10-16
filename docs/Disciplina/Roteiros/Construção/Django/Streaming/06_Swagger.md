# 06 - Documentação da API (Swagger/OpenAPI)

## Introdução à Documentação da API

Para adicionar documentação moderna ao seu projeto Django com Django REST Framework, utilizaremos a biblioteca **drf-spectacular**. Esta é a biblioteca mais atual e recomendada para gerar documentação OpenAPI 3.0, substituindo o `drf-yasg` que foi descontinuado.

### Por que usar drf-spectacular?

- ✅ **Moderno**: Suporte completo ao OpenAPI 3.0
- ✅ **Ativo**: Biblioteca mantida e atualizada regularmente
- ✅ **Performático**: Melhor performance que o drf-yasg
- ✅ **Recursos avançados**: Suporte a schemas complexos e customizações

### Passos para Configurar com `drf-spectacular`

1. **Instalar o `drf-spectacular`**

   Execute o seguinte comando para instalar a biblioteca:

   ```bash
   pip install drf-spectacular
   ```

2. **Configurar o `drf-spectacular` no Projeto**

   **2.1. Adicionar ao `settings.py`:**

   ```python
   # settings.py
   INSTALLED_APPS = [
       # outros apps padrão
       'rest_framework',
       'drf_spectacular',  # Adicionar aqui
       'content_app',
   ]

   # Configuração do Django REST Framework
   REST_FRAMEWORK = {
       'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
       'DEFAULT_AUTHENTICATION_CLASSES': [
           'rest_framework.authentication.SessionAuthentication',
       ],
       'DEFAULT_PERMISSION_CLASSES': [
           'rest_framework.permissions.IsAuthenticatedOrReadOnly',
       ],
   }

   # Configurações do drf-spectacular
   SPECTACULAR_SETTINGS = {
       'TITLE': 'Streaming Platform API',
       'DESCRIPTION': 'API completa para plataforma de streaming de áudio e vídeo',
       'VERSION': '1.0.0',
       'SERVE_INCLUDE_SCHEMA': False,
       'COMPONENT_SPLIT_REQUEST': True,
       'SORT_OPERATIONS': False,
       'TAGS': [
           {'name': 'Authentication', 'description': 'Endpoints de autenticação'},
           {'name': 'Content', 'description': 'Gerenciamento de conteúdo'},
           {'name': 'Playlists', 'description': 'Gerenciamento de playlists'},
           {'name': 'Users', 'description': 'Gerenciamento de usuários'},
       ],
   }
   ```

   **2.2. Configurar URLs no projeto:**

   Abra o arquivo `urls.py` do seu projeto Django e adicione as seguintes configurações:

   ```python
   # streaming_platform/urls.py
   from django.contrib import admin
   from django.urls import path, include
   from drf_spectacular.views import (
       SpectacularAPIView,
       SpectacularRedocView,
       SpectacularSwaggerView,
   )

   urlpatterns = [
       # URLs do admin
       path('admin/', admin.site.urls),
       
       # URLs da API
       path('api/', include('content_app.urls')),
       
       # URLs da documentação
       path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
       path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
       path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
   ]
   ```

3. **Acessar a Documentação da API**

   Com a configuração acima, você terá acesso a três tipos de documentação:

   * **Schema OpenAPI**: Especificação completa da API em formato JSON/YAML:
     ```plaintext
     http://localhost:8000/api/schema/
     ```

   * **Swagger UI**: Interface interativa moderna para testar a API:
     ```plaintext
     http://localhost:8000/api/docs/
     ```

   * **ReDoc**: Interface de documentação elegante e responsiva:
     ```plaintext
     http://localhost:8000/api/redoc/
     ```

4. **Personalizar a Documentação com Decorators**

   Use decorators do `drf-spectacular` para melhorar a documentação:

   ```python
   # views.py
   from rest_framework import viewsets
   from drf_spectacular.utils import extend_schema, extend_schema_view
   from .models import Content
   from .serializers import ContentSerializer

   @extend_schema_view(
       list=extend_schema(
           description="Lista todos os conteúdos públicos",
           tags=["Content"]
       ),
       create=extend_schema(
           description="Cria um novo conteúdo (requer autenticação)",
           tags=["Content"]
       ),
       retrieve=extend_schema(
           description="Obtém detalhes de um conteúdo específico",
           tags=["Content"]
       ),
       update=extend_schema(
           description="Atualiza um conteúdo existente (apenas o criador)",
           tags=["Content"]
       ),
       destroy=extend_schema(
           description="Remove um conteúdo (apenas o criador)",
           tags=["Content"]
       ),
   )
   class ContentViewSet(viewsets.ModelViewSet):
       queryset = Content.objects.filter(is_public=True)
       serializer_class = ContentSerializer

       def perform_create(self, serializer):
           serializer.save(creator=self.request.user)
   ```

5. **Customizar Serializers para Melhor Documentação**

   ```python
   # serializers.py
   from rest_framework import serializers
   from drf_spectacular.utils import extend_schema_field
   from .models import Content

   class ContentSerializer(serializers.ModelSerializer):
       creator_name = serializers.SerializerMethodField()
       
       class Meta:
           model = Content
           fields = [
               'id', 'title', 'description', 'file_url', 
               'content_type', 'is_public', 'creator_name'
           ]
           read_only_fields = ['id', 'creator_name']

       @extend_schema_field(serializers.CharField)
       def get_creator_name(self, obj):
           """Retorna o nome do criador do conteúdo"""
           return obj.creator.username
   ```

### Recursos Avançados do drf-spectacular

1. **Personalização de Esquemas Complexos**

   ```python
   from drf_spectacular.utils import extend_schema, OpenApiExample
   from drf_spectacular.openapi import AutoSchema

   @extend_schema(
       request=ContentSerializer,
       responses={201: ContentSerializer},
       examples=[
           OpenApiExample(
               "Exemplo de Vídeo",
               summary="Criação de conteúdo de vídeo",
               description="Exemplo de como criar um novo vídeo",
               value={
                   "title": "Meu Vídeo Incrível",
                   "description": "Descrição do vídeo",
                   "content_type": "video",
                   "is_public": True
               },
               request_only=True,
           ),
           OpenApiExample(
               "Exemplo de Áudio",
               summary="Criação de conteúdo de áudio",
               description="Exemplo de como criar um novo áudio",
               value={
                   "title": "Minha Música",
                   "description": "Descrição da música",
                   "content_type": "audio",
                   "is_public": False
               },
               request_only=True,
           ),
       ]
   )
   def create(self, request, *args, **kwargs):
       return super().create(request, *args, **kwargs)
   ```

2. **Configuração de Autenticação na Documentação**

   ```python
   # settings.py
   SPECTACULAR_SETTINGS = {
       # ... outras configurações ...
       'SECURITY': [
           {
               'type': 'http',
               'scheme': 'bearer',
               'bearerFormat': 'JWT',
           }
       ],
       'COMPONENT_SPLIT_REQUEST': True,
       'SWAGGER_UI_SETTINGS': {
           'deepLinking': True,
           'persistAuthorization': True,
           'displayOperationId': True,
       },
   }
   ```

3. **Filtros e Paginação na Documentação**

   ```python
   from django_filters import rest_framework as filters
   from drf_spectacular.utils import extend_schema_view, extend_schema

   class ContentFilter(filters.FilterSet):
       content_type = filters.CharFilter(field_name='content_type')
       is_public = filters.BooleanFilter(field_name='is_public')
       
       class Meta:
           model = Content
           fields = ['content_type', 'is_public']

   @extend_schema_view(
       list=extend_schema(
           parameters=[
               OpenApiParameter(
                   name='content_type',
                   description='Filtrar por tipo de conteúdo',
                   required=False,
                   type=str,
                   enum=['video', 'audio']
               ),
           ]
       )
   )
   class ContentViewSet(viewsets.ModelViewSet):
       queryset = Content.objects.all()
       serializer_class = ContentSerializer
       filterset_class = ContentFilter
   ```

### Migração do drf-yasg para drf-spectacular

Se você está migrando de `drf-yasg`, siga estes passos:

1. **Remover drf-yasg**:
   ```bash
   pip uninstall drf-yasg
   ```

2. **Instalar drf-spectacular**:
   ```bash
   pip install drf-spectacular
   ```

3. **Atualizar settings.py**:
   - Remover `drf_yasg` do `INSTALLED_APPS`
   - Adicionar `drf_spectacular`
   - Adicionar configurações do `SPECTACULAR_SETTINGS`

4. **Atualizar urls.py**:
   - Substituir imports do `drf_yasg` pelos do `drf_spectacular`

5. **Atualizar decorators**:
   - Substituir `@swagger_auto_schema` por `@extend_schema`

### Comandos Úteis

```bash
# Gerar schema estático
python manage.py spectacular --color --file schema.yml

# Validar schema
python manage.py spectacular --validate

# Gerar documentação em HTML
python manage.py spectacular --format openapi-json --file openapi-schema.json
```

### Configuração Opcional Avançada

Para personalizar ainda mais a documentação, você pode:

1. **Criar schemas customizados**
2. **Adicionar autenticação específica**
3. **Configurar versionamento da API**
4. **Personalizar a interface Swagger UI**

```python
# settings.py - Configuração avançada
SPECTACULAR_SETTINGS = {
    'TITLE': 'Streaming Platform API',
    'DESCRIPTION': 'API completa para plataforma de streaming',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'CONTACT': {
        'name': 'Suporte Técnico',
        'email': 'suporte@streaming.com',
        'url': 'https://streaming.com/suporte',
    },
    'LICENSE': {
        'name': 'MIT License',
        'url': 'https://opensource.org/licenses/MIT',
    },
    'SWAGGER_UI_SETTINGS': {
        'deepLinking': True,
        'persistAuthorization': True,
        'displayOperationId': True,
        'filter': True,
        'tryItOutEnabled': True,
    },
    'REDOC_UI_SETTINGS': {
        'hideDownloadButton': False,
        'hideHostname': False,
        'hideLoading': False,
        'hideSchemaPattern': True,
        'scrollYOffset': 0,
        'theme': {
            'colors': {
                'primary': {
                    'main': '#1976d2'
                }
            }
        }
    }
}
```

---

### Vantagens do drf-spectacular sobre drf-yasg

| Aspecto | drf-yasg | drf-spectacular |
|---------|----------|-----------------|
| **Status** | ⚠️ Descontinuado | ✅ Ativo |
| **OpenAPI** | 2.0 | 3.0+ |
| **Performance** | ⚠️ Mais lento | ✅ Otimizado |
| **Manutenção** | ❌ Sem suporte | ✅ Mantido |
| **Recursos** | ⚠️ Limitados | ✅ Completos |

O `drf-spectacular` oferece uma solução moderna, robusta e bem mantida para documentação de APIs Django REST Framework, sendo a escolha recomendada para novos projetos e migrações.
