from rest_framework.serializers import ModelSerializer, SerializerMethodField

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
        fields = ("id", "quantity", "price", "product", "outlet", "isOffered")


class InventorySerializer(ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Inventory
        fields = ("id", "quantity", "price", "product", "outlet", "isOffered")


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


class SubCategoryProductObectSerializer(ModelSerializer):
    class Meta:
        model = SubCategoryProduct
        fields = "__all__"


class ProductInventorySerializer(ModelSerializer):
    # outlet_inventory = InventoryInlineSerializer(
    # source="product_inventory_product", many=True)

    outlet_inventory = SerializerMethodField('get_outlet_only_inventory')

    def get_outlet_only_inventory(self, product):
        found_inventory = Inventory.objects.get(
            outlet__id=self.context["outlet_id"], product__id=product.id)
        serializer = InventoryInlineSerializer(
            instance=found_inventory, many=False)
        return serializer.data

    class Meta:
        model = Product
        fields = ("id", "name", "display_name", "thumbnail", "description",
                  "price", "brand", "size", "variant", "size", "color",
                  "outlet_inventory")


class CreateProductInventorySerializer(ModelSerializer):
    product = ProductSerializer
    class Meta:
        model = Inventory
        fields = "__all__"


class CollectionProductSerializer(ModelSerializer):
    product = ProductInventorySerializer()

    class Meta:
        model = CollectionProduct
        fields = "__all__"