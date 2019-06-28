from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from product_collections.models import Collection
from store_listing.models import Store

from product_collections.serializers import CollectionProductsDetailSerializer


#TODO phose out and switch completely to StoreCollectionInventoryView
class StoreCollectionsView(ListAPIView):
    #show a list of all collections in a specific store
    permission_classes = [
        AllowAny,
    ]
    model = Collection
    serializer_class = CollectionProductsDetailSerializer

    def get_queryset(self):
        """
        Get list of collections for the store 
        """
        store_id = self.kwargs['id']
        return Collection.objects.filter(store=Store.objects.get(id=store_id))
