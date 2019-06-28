from django.conf import settings
from django.conf.urls import url
from .api import SubCategoryProductsView
from .api import ProductListView, InventoryListView, UpdateProductPrice, OutletSubcategoryInventoryView, StoreCollectionInventoryView

app_name = "product_listing"

subcategory_product_urls = [
    url(r'^$', SubCategoryProductsView.as_view(), name="subcategory-products"),
]

outlet_subcategory_inventory_urls = [
    url(r'^$',
        OutletSubcategoryInventoryView.as_view(),
        name='outlet-subcategory-inventory-view'),
]
store_collection_inventory_urls = [
    url(r'^$',
        StoreCollectionInventoryView.as_view(),
        name='store-collection-inventory-view'),
]

api_product_urls = [
    # used to search for products in an outlet
    url(r'^$', InventoryListView.as_view(), name='outlet-products-view'),
    url(r'^update-product-price/$',
        UpdateProductPrice.as_view(),
        name='update-product-price-view'),
]