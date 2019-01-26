from rest_framework.generics import RetrieveAPIView

from .serializers import SubCategoryProductListSerializer
from categories.models import SubCategory

class SubCategoryProductsView(RetrieveAPIView):
    model= SubCategory
    queryset= SubCategory.objects.all()
    lookup_url_kwarg="subcategory_id"
    lookup_field="id"
    serializer_class = SubCategoryProductListSerializer