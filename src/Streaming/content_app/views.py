from rest_framework import viewsets
from .models import Content
from .serializers import ContentSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    #permission_classes = [IsAuthenticatedOrReadOnly]

<<<<<<< HEAD
    #def perform_create(self, serializer):
    #    serializer.save(creator=self.request.user)
=======
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
>>>>>>> e0e89c1b5bc9960be6613bc2bbcc94462c287a9d
