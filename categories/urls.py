from django.conf import settings
from django.conf.urls import url, include
from .api import StoreCategoriesView, CategorySubCategoriesView, SearchSubCategoryView, CreateCategoryAPIView

from product_listing.urls import subcategory_product_urls, subcategory_inventory_urls

app_name = "categories"

store_categories_urls = [
    url(r'^create/', CreateCategoryAPIView.as_view(), name='create-categories'),
    url(r'^$', StoreCategoriesView.as_view(), name='store-categories'),
    url(r'^(?P<category_id>\d+)/subcategories/$',
        CategorySubCategoriesView.as_view(),
        name="category-subcategories"),
    url(
        r'^(?P<category_id>\d+)/subcategories/(?P<subcategory_id>\d+)/products/$',
        include(subcategory_product_urls)),
]

outlet_subcategories_urls = [
    url(r'^(?P<subcategory_id>\d+)/inventory/$',
        include(subcategory_inventory_urls)),
    url(r'^$', SearchSubCategoryView.as_view(), name='search-subcategory'),
]
