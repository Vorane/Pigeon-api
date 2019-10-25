from rest_framework.serializers import ModelSerializer

from store_listing.models import Store
from .models import Category, SubCategory, CategorySubCategory
from store_listing.serializers import StoreSerializer


class SubCategorySerializer(ModelSerializer):
    class Meta:
        model = SubCategory
        fields = "__all__"


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CategorySubCategorySerializer(ModelSerializer):
    category = CategorySerializer()
    sub_category = SubCategorySerializer()

    class Meta:
        model = CategorySubCategory
        fields = ("id", "sub_category", "category")


class CategorySubCategoryListingSerializer(ModelSerializer):
    sub_categories = CategorySubCategorySerializer(
        many=True, source="category_categorysubcategory")

    class Meta:
        model = Category
        fields = ("id", "name", "sub_categories")


class CategoryDetailSerializer(ModelSerializer):
    category_subcategories = CategorySubCategorySerializer(
        many=True, source="category_categorysubcategory")

    class Meta:
        model = Category
        fields = ("name", "display_name", "id", "category_subcategories",
                  "thumbnail", "description", "color", "store")


class StoreCategorySerializer(ModelSerializer):
    categories = CategoryDetailSerializer(many=True, source="store_category")

    class Meta:
        model = Store
        fields = ("id", "name", "categories")
