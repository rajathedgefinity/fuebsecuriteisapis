from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name="hello"),
    path('api-token-auth', obtain_auth_token, name="api_token_auth"),
    path('visitor-management', views.VisitorManagement.as_view(), name="visitormanagement"),
    path('user-management', views.UserManagement.as_view(), name="usermanagement"),
    path('delivery-management', views.DeliveryManagement.as_view(), name="deliverymanagement"),
]
