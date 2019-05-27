from rest_framework.serializers import ModelSerializer
from product_listing.serializers import CollectionProductSerializer

from product_collections.models import Collection


class CollectionProductsDetailSerializer(ModelSerializer):
    products = CollectionProductSerializer(
        many=True, source="collection_collection_product")

    class Meta:
        model = Collection
        fields = "__all__"
