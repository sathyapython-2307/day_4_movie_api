# ...existing code...
import django_filters
from .models import Movie

class MovieFilter(django_filters.FilterSet):
    release_date = django_filters.DateFromToRangeFilter()
    rating = django_filters.NumericRangeFilter()
    genre = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Movie
        fields = ['genre', 'release_date', 'rating']
