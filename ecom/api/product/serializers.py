from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.HyperlinkedModelSerializer):
 image = serializers.ImageField(max_length=None, allow_empty_file=False, allow_null=True, required=True)
 class Meta:
  model = Product
  fields = ('name','description','price','stock','is_active','image','category')