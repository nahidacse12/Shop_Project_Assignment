from rest_framework import serializers
from .models import Product
class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, allow_blank=False, trim_whitespace=True)
    price = serializers.DecimalField(max_digits=10, decimal_places=2, min_value=0.01)
    stock = serializers.IntegerField(min_value=0)
    class Meta:
        model=Product
        fields=['id','name','description','price','stock']
        read_only_fields=['id']
    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError('Product name cannot be empty.')
        return value.strip()
