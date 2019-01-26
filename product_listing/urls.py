from django.conf import settings
from django.conf.urls import url
from .api import SubCategoryProductsView

app_name = "product_listing"

subcategory_product_urls = [    
    url(r'^$',  SubCategoryProductsView.as_view() ,name="subcategory-products" ),
]

