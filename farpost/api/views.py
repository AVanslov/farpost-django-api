from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from .models import Add
from .serializers import AddSerializer


class AddViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Add.objects.all()
    serializer_class = AddSerializer
    lookup_field = 'add_id'

    def get_object(self):
        return get_object_or_404(Add, id=self.kwargs['add_id'])
