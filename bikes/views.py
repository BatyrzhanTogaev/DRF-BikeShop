from rest_framework import viewsets, permissions, filters
from .models import Bike
from .serializers import BikeSerializers
from .permissions import IsOwnerOrReadOnly


class BikeViewSet(viewsets.ModelViewSet):
    queryset = Bike.objects.all()
    serializer_class = BikeSerializers
    permission_classes = {
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly}

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['brand', 'model']
    ordering_fields = ['year', 'created_at']
