from rest_framework.serializers import ModelSerializer

from categories.models import SubCategory
from categories.serializers import SubCategorySerializer
from .models import Product, SubCategoryProduct, Inventory, CollectionProduct
from product_collections.models import Collection


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductInlineSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "name")


class InventoryInlineSerializer(ModelSerializer):
    class Meta:
        model = Inventory
        fields = ("id", "quantity", "price", "product", "outlet")


class InventorySerializer(ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Inventory
        fields = ("id", "quantity", "price", "product", "outlet")


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


class ProductInventorySerializer(ModelSerializer):
    outlet_inventory = InventoryInlineSerializer(
        source="product_inventory_product", many=True)

    class Meta:
        model = Product
        fields = ("id", "name", "display_name", "thumbnail", "description",
                  "price", "brand", "size", "variant", "size", "color",
                  "outlet_inventory")


class CollectionProductSerializer(ModelSerializer):
    product = ProductInventorySerializer()

    class Meta:
        model = CollectionProduct
        fields = "__all__"