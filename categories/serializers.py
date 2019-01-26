from  rest_framework.serializers import ModelSerializer

from store_listing.models import Store
from .models import Category

class CategorySerializer(ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"

class StoreCategorySerializer(ModelSerializer):
    categories = CategorySerializer(many=True, source="store_category")
    class Meta:
        model = Store
        fields = ("id","name","categories")