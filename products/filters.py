import django_filters
from .models import Product
from django_filters import DateFilter, CharFilter, AllValuesFilter, OrderingFilter


class ProductFilter(django_filters.FilterSet):
    # price = django_filters.NumberFilter()
    # price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    # price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
    manufacturer = django_filters.AllValuesFilter(field_name="manufacturer")
    make = django_filters.AllValuesFilter(field_name="make")
    model = django_filters.AllValuesFilter(field_name="model")
    
    o = OrderingFilter(
        fields ={
        ('build_year', 'build_year'),
        ('price', 'price')
        }
    )
    
    
    # build_year = DateFilter(field)
    class Meta:
        model = Product
        fields = ['manufacturer', 'make', 'model']
        # exclude = ['image_main', 'image_sec', 'original_key']