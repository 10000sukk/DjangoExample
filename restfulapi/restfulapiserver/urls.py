from django.conf.urls import url
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from addresses import views


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('addresses/', views.address_list),
    # path('addresses/<int:pk>/', views.address),
    # path('login/',views.login),
    path('app_login/',views.app_login),
    path('app_register/', views.app_register),
    path('api/boards/',views.app_board),
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]