from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import ValidationError,CharField,EmailField
from .models import User

User = get_user_model()


class AccountCreateSerializer(serializers.ModelSerializer):
    class Meta:
        """ Account serializer """
        model = User
        fields = ['id', 'user_uuid', 'username','phone_number', 'email', 'password']
        extra_kwargs = {"password":{"write_only": True}}

    def create(self, validated_data):
        username = validated_data['username']
        phone_number = validated_data['phone_number']
        email = validated_data['email']
        password = validated_data['password']

        user = User(phone_number = phone_number, username = username, email = email)
        user.set_password(password)
        user.save()
        return user