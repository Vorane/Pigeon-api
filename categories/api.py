from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from store_listing.models import Store
from .models import Category, SubCategory
from .serializers import StoreCategorySerializer, CategorySubCategoryListingSerializer, SubCategorySerializer
from rest_framework import filters


class CategorySubCategoriesView(RetrieveAPIView):
    permission_classes = [AllowAny,]
    model = Category
    lookup_url_kwarg="category_id"
    lookup_field="id"
    queryset = Category.objects.all()
    serializer_class= CategorySubCategoryListingSerializer


class StoreCategoriesView(RetrieveAPIView):
    permission_classes = [AllowAny,]
    model=Store
    lookup_field="id"
    queryset=Store.objects.all()
    serializer_class = StoreCategorySerializer


class SearchSubCategoryView(ListAPIView):
    permission_classes = [AllowAny, ]
    search_fields = ['name', 'display_name']
    filter_backends = (filters.SearchFilter,)
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
