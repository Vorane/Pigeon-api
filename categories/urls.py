from django.conf import settings
from django.conf.urls import url, include
from .api import StoreCategoriesView, CategorySubCategoriesView

from product_listing.urls import subcategory_product_urls

app_name = "categories"

store_categories_urls = [
    url(r'^$', StoreCategoriesView.as_view(), name='store-categories'),
    url(r'^(?P<category_id>\d+)/subcategories/$',  CategorySubCategoriesView.as_view() ,name="category-subcategories" ),
    url(r'^(?P<category_id>\d+)/subcategories/(?P<subcategory_id>\d+)/products/$', include(subcategory_product_urls)),
    
]


