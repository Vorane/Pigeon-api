from django.conf import settings
from django.conf.urls import url
from .api import SubCategoryProductsView
from .api import ProductListView, InventoryListView, UpdateProductPrice, OutletSubcategoryProductsView, StoreCollectionInventoryView, UpdateInventoryView, \
    CreateProductInventoryView, CreateProductMappingView

app_name = "product_listing"

subcategory_product_urls = [
    url(r'^$', SubCategoryProductsView.as_view(), name="subcategory-products"),
]

subcategory_inventory_urls = [
    url(r'^$',
        OutletSubcategoryProductsView.as_view(),
        name='outlet-subcategory-inventory-view'),
]
store_collection_inventory_urls = [
    url(r'^$',
        StoreCollectionInventoryView.as_view(),
        name='store-collection-inventory-view'),
]

outlet_product_urls = [
    # used to search for products in an outlet
    url(r'^$', InventoryListView.as_view(), name='outlet-products-view'),
    url(r'^update-product-price/$',
        UpdateProductPrice.as_view(),
        name='update-product-price-view'),
    url(r'^create/', CreateProductInventoryView.as_view(), name='create-products-inventory'),
    url(r'^map/', CreateProductMappingView.as_view(), name='create-product-subcategory-mapping'),
]

outlet_inventory_urls = [
    url(r'^(?P<inventory_id>\d+)/update/$',
        UpdateInventoryView.as_view(),
        name='update-outlet-inventory-view'),
]