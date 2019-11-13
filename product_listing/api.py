from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView, ListAPIView, UpdateAPIView, ListCreateAPIView, CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import filters

from categories.models import SubCategory
from commons.utils import validate_object
from .models import SubCategoryProduct
from product_listing.models import Product, Inventory
from product_listing.serializers import ProductSerializer, InventorySerializer
from .serializers import SubCategoryProductListSerializer, ProductInventorySerializer, CreateProductInventorySerializer, SubCategoryProductObectSerializer
from .permissions import IsAllowedInventoryUpdate


#TODO phase out subCategoryProductsView for OutletSubcategoryView
class SubCategoryProductsView(RetrieveAPIView):
    permission_classes = [
        AllowAny,
    ]
    model = SubCategory
    queryset = SubCategory.objects.all()
    lookup_url_kwarg = "subcategory_id"
    lookup_field = "id"
    serializer_class = SubCategoryProductListSerializer


class OutletSubcategoryProductsView(ListAPIView):
    permission_classes = [
        AllowAny,
    ]
    model = Product
    serializer_class = ProductInventorySerializer

    def get_serializer_context(self):
        return {"outlet_id": self.kwargs['outlet_id']}

    def get_queryset(self):
        """
        This view should return a list of all the inventory for
        an outlet that belong to the subcategory submitted.
        """
        outlet_id = self.kwargs['outlet_id']
        subcategory_id = self.kwargs['subcategory_id']
        return Product.objects.filter(
            product_inventory_product__outlet__id=outlet_id,
            product_subcategory_product__sub_category=subcategory_id)


class StoreCollectionInventoryView(ListAPIView):
    permission_classes = [
        AllowAny,
    ]
    model = Inventory
    serializer_class = InventorySerializer

    def get_serializer_context(self):
        return {"outlet_id": self.kwargs['outlet_id']}

    def get_queryset(self):
        """
        This view should return a list of all the inventory for
        an outlet that belong to the subcategory submitted.
        """
        store_id = self.kwargs['store_id']
        outlet_id = self.kwargs['store_id']
        return Inventory.objects.filter(
            isOffered=True,
            product__product_colection_product__collection__store=store_id,
        )


class ProductListView(ListAPIView):
    permission_classes = [
        AllowAny,
    ]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('display_name', )


class InventoryListView(ListAPIView):
    permission_classes = [
        AllowAny,
    ]
    queryset = Product.objects.all()
    serializer_class = ProductInventorySerializer

    def get_serializer_context(self):
        return {"outlet_id": self.kwargs['outlet_id']}

    def get_queryset(self):
        """
        This view should return a list of all the products for
        an outlet as determined by the outlet_id portion of the URL.
        """
        outlet_id = self.kwargs['outlet_id']
        return Product.objects.filter(
            product_inventory_product__outlet__id=outlet_id).order_by(
                'display_name')

    filter_backends = (filters.SearchFilter, )
    search_fields = ('display_name', )


class UpdateProductPrice(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    #handle the post methon
    def post(self, request, **kwargs):
        if request.data:
            #check if payload has required fields
            valid = validate_object(request.data, ["product_id", "new_price"])
            if not valid["status"]:
                return JsonResponse(
                    {
                        'status': 'bad request',
                        'message': "missing attribute: " + valid["field"]
                    },
                    status=400)

            try:
                found_product = Product.objects.get(
                    id=request.data["product_id"])
                #get the product with corresponding id
                #update the product and save
                found_product.price = request.data["new_price"]
                found_product.save()
                return JsonResponse(
                    {
                        'status': 'product successfully update',
                        'message': "The product has been successfully updated"
                    },
                    status=200)

            except Product.DoesNotExist:
                #show error for product not found
                return JsonResponse({
                    'status':
                    'product not found',
                    'message':
                    "Unable to find the product with the given product id"
                },
                                    status=404)
        else:
            #show error for product not found
            return JsonResponse({
                'status': 'bad request',
                'message': "no data provided in request body"
            },
                                status=400)


class UpdateInventoryView(UpdateAPIView):
    permission_classes = [AllowAny,]
    serializer_class = InventorySerializer
    model = Inventory
    queryset = Inventory.objects.all()
    lookup_url_kwarg = "inventory_id"


class CreateProductInventoryView(CreateAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = CreateProductInventorySerializer
    model = Inventory

    def post(self, request, *args, **kwargs):
        product_data = request.data.pop('product')
        product = Product.objects.create(**product_data)
        data = {
            "product" : product.id,
            "outlet" :request.data['outlet'],
            "quantity" : request.data['quantity'],
            "isOffered": request.data['isOffered'],
            "price" : request.data['price']
        }
        serializer_class = CreateProductInventorySerializer(data=data)
        if serializer_class.is_valid():
            inventory = serializer_class.save()
            print("Product val {}".format(product_data))
            return JsonResponse({
                "status" : "ok",
                "message" : "product and inventory added successfully"
            }, status=200)
        else:
            return JsonResponse({
                "status": "false",
                "message": "Invalid data"
            }, status=400)


class CreateProductMappingView(ListCreateAPIView):
    permission_classes = [AllowAny,]
    serializer_class = SubCategoryProductObectSerializer
    queryset = SubCategoryProduct.objects.all()
