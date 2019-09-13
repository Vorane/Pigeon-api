from rest_framework.serializers import ModelSerializer
from push_notifications.models import GCMDevice


class FCMDeviceSerializer(ModelSerializer):
    """ Create dock bikes serializer """

    class Meta:
        """ Meta class for bike request create serializer """
        model = GCMDevice
        fields = '__all__'