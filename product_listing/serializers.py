from rest_framework.serializers import ModelSerializer


from categories.models import SubCategory
from categories.serializers import SubCategorySerializer
from .models import Product, SubCategoryProduct

class ProductSerializer(ModelSerializer):
    class Meta:
        model=Product
        fields="__all__"

class SubCategoryProductSerializer(ModelSerializer):
    sub_category = SubCategorySerializer()
    product = ProductSerializer()
    
    class Meta:
        model=SubCategoryProduct
        fields="__all__"


class SubCategoryProductListSerializer(ModelSerializer):
    products = SubCategoryProductSerializer(many=True, source="subcategory_subcategory_product")
    class Meta:
        model=SubCategory
        fields=("id","name","products")
