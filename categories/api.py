from rest_framework.generics import RetrieveAPIView, ListAPIView, ListCreateAPIView, CreateAPIView
from rest_framework.permissions import AllowAny
from store_listing.models import Store
from .models import Category, SubCategory, CategorySubCategory
from .serializers import StoreCategorySerializer, CategorySubCategoryListingSerializer, SubCategorySerializer, CategorySerializer, CategorySubCategoryInlineSerializer
from rest_framework import filters
from django.http import JsonResponse
from store_listing.models import Outlet


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


class CreateCategoryAPIView(ListCreateAPIView):
    permission_classes = [AllowAny, ]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def post(self, request, *args, **kwargs):
        data = {
            "name" : request.data['name'],
            "display_name" :request.data['display_name'],
            "store" :kwargs['id']
        }
        subcategory_serializer= SubCategorySerializer(data=data)
        if subcategory_serializer.is_valid():
            subcategory_serializer.save()
        return self.create(request, *args, **kwargs)


class CreateSubCategoryView(CreateAPIView):
    permission_classes = [AllowAny, ]
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class CreateSubCategoryMappingView(ListCreateAPIView):
    permission_classes = [AllowAny, ]
    queryset = CategorySubCategory.objects.all()
    serializer_class = CategorySubCategoryInlineSerializer