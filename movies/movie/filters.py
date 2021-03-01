from django_filters import FilterSet,CharFilter
from .models import *

class MoviesFilter(FilterSet):
    name = CharFilter(lookup_expr='icontains')
    class Meta:
        model = Movies
        fields = ['name','genre']
