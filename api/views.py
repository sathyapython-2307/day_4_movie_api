# ...existing code...
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from .models import Movie
from .serializers import MovieSerializer
from .filters import MovieFilter

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().order_by('-rating', 'release_date')
    serializer_class = MovieSerializer
    filterset_class = MovieFilter
    filter_backends = [OrderingFilter]
    ordering_fields = ['release_date', 'rating']
    ordering = ['-rating', 'release_date']  # Default ordering
