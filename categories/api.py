from rest_framework.generics import RetrieveAPIView

from store_listing.models import Store
from .models import Category
from .serializers import StoreCategorySerializer, CategorySubCategoryListingSerializer


class CategorySubCategoriesView(RetrieveAPIView):
    model = Category
    lookup_url_kwarg="category_id"
    lookup_field="id"
    queryset = Category.objects.all()
    serializer_class= CategorySubCategoryListingSerializer


class StoreCategoriesView(RetrieveAPIView):
    model=Store
    lookup_field="id"
    queryset=Store.objects.all()
    serializer_class = StoreCategorySerializer