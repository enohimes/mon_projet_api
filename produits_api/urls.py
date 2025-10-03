from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProduitAPIView
from .views import CreateUserView, LoginView

urlpatterns = [
    path('produits/', ProduitAPIView.as_view(), name='produit-list'),
    path('auth/register/', CreateUserView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
]