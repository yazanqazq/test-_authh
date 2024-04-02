from django.shortcuts import render
from rest_framework import viewsets ,permissions
from .models import *
from django.contrib.auth.models import User
from .serializer import *
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import MethodNotAllowed
from rest_framework import status

# Create your views here.
# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class Viewsets_show_all_address_customer(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer 
    permission_classes = [permissions.IsAuthenticated]
    
class Viewsets_show_all_tools(viewsets.ModelViewSet):
    queryset = Tools.objects.all()
    serializer_class = ToolsSerializer
    
    
class Viewsets_order(viewsets.ModelViewSet):
    queryset = Order.objects.none()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user)

    def perform_create(self, serializer):
        # Set the user of the address to the current authenticated user
        serializer.save(customer=self.request.user)
    
    
    

class Viewsets_my_tools(viewsets.ModelViewSet):
    queryset = Tools.objects.none()
    serializer_class = ToolsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Tools.objects.filter(customer=self.request.user)

    def perform_create(self, serializer):
        # Set the user of the address to the current authenticated user
        serializer.save(customer=self.request.user)
    
    