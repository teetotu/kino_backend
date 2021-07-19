from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token

from .models import Location


class LocationSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = (
            'id',
            'Link',
            'Title',
            'get_absolute_url',
            'get_first_photo',
            'get_photos',
            'get_descriptions',
            'Address'
        )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']

        extra_kwargs = {
            'password': {
                'write_only' : True
            }
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user
