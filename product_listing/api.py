from rest_framework.generics import RetrieveAPIView , ListAPIView
from rest_framework import filters

from .serializers import SubCategoryProductListSerializer
from categories.models import SubCategory
from product_listing.models import Product , Inventory
from product_listing.serializers import ProductSerializer , InventorySerializer

class SubCategoryProductsView(RetrieveAPIView):
    model= SubCategory
    queryset= SubCategory.objects.all()
    lookup_url_kwarg="subcategory_id"
    lookup_field="id"
    serializer_class = SubCategoryProductListSerializer

class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('display_name',)

class InventoryListView(ListAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('product__display_name',)