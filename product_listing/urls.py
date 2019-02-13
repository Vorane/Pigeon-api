from django.conf import settings
from django.conf.urls import url
from .api import SubCategoryProductsView
from .api import ProductListView

app_name = "product_listing"

subcategory_product_urls = [    
    url(r'^$',  SubCategoryProductsView.as_view() ,name="subcategory-products" ),
]

api_product_urls = [
    # used to search for products in an outlet
    url(r'^$',ProductListView.as_view(),
        name='outlet-products-view'),
   
]