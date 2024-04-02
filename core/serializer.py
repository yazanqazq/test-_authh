from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from .models import *

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
      model =Address
      fields='__all__'


class ToolsSerializer(serializers.ModelSerializer):
    class Meta:
      model =Tools
      fields='__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
      model =Order
      fields='__all__'