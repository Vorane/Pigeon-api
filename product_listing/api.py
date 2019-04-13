from rest_framework.generics import RetrieveAPIView , ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework import filters

from .serializers import SubCategoryProductListSerializer
from categories.models import SubCategory
from product_listing.models import Product , Inventory
from product_listing.serializers import ProductSerializer , InventorySerializer

class SubCategoryProductsView(RetrieveAPIView):
    permission_classes = [AllowAny,]
    model= SubCategory
    queryset= SubCategory.objects.all()
    lookup_url_kwarg="subcategory_id"
    lookup_field="id"
    serializer_class = SubCategoryProductListSerializer

class ProductListView(ListAPIView):
    permission_classes = [AllowAny,]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('display_name',)

class InventoryListView(ListAPIView):
    permission_classes = [AllowAny,]
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    def get_queryset(self):
        """
        This view should return a list of all the inventory for
        an outlet as determined by the outlet_id portion of the URL.
        """
        outlet_id = self.kwargs['outlet_id']
        return Inventory.objects.filter(outlet__id=outlet_id).order_by('product.display_name')
    
    filter_backends = (filters.SearchFilter,)
    search_fields = ('product__display_name',)