from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from products.api import viewsets as productsviewsets
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

route = routers.DefaultRouter()

route.register('api/product', productsviewsets.ProductsViewSet)
route.register('api/customer', productsviewsets.CustomersViewSet)

urlpatterns = [
	path('token/', TokenObtainPairView.as_view()),
	path('token/refresh/', TokenRefreshView.as_view()),
	path('admin/', admin.site.urls),
	path('', include(route.urls))
]
