from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from products.api import viewsets as productsviewsets

route = routers.DefaultRouter()

route.register('api/product', productsviewsets.ProductsViewSet)
route.register('api/customer', productsviewsets.CustomersViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))
]
