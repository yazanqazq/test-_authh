from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from core. views import *



# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('show_all_customer',Viewsets_show_all_address_customer)
router.register('show_all_tools',Viewsets_show_all_tools, basename='all_tools')
router.register('order',Viewsets_order)
router.register('my_tools',Viewsets_my_tools, basename='my_tools')
router.register('Categories',Viewsets_show_all_Categories, basename='Categories')

# router.register('exam', ExampleView)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls'))
]