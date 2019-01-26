from rest_framework.generics import RetrieveAPIView

from store_listing.models import Store

from .serializers import StoreCategorySerializer

class StoreCategoriesView(RetrieveAPIView):
    model=Store
    lookup_field="id"
    queryset=Store.objects.all()
    serializer_class = StoreCategorySerializer