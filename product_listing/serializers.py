from rest_framework.serializers import ModelSerializer

from categories.models import SubCategory
from categories.serializers import SubCategorySerializer
from .models import Product, SubCategoryProduct, Inventory, CollectionProduct
from product_collections.models import Collection


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class InventorySerializer(ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Inventory
        fields = ("id", "quantity", "product")


class SubCategoryProductSerializer(ModelSerializer):
    sub_category = SubCategorySerializer()
    product = ProductSerializer()

    class Meta:
        model = SubCategoryProduct
        fields = "__all__"


class SubCategoryProductListSerializer(ModelSerializer):
    products = SubCategoryProductSerializer(
        many=True, source="subcategory_subcategory_product")

    class Meta:
        model = SubCategory
        fields = ("id", "name", "products")


class CollectionProductSerializer(ModelSerializer):
    class Meta:
        model = CollectionProduct
        fields = "__all__"


