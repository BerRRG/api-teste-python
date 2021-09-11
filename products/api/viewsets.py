from rest_framework import viewsets
from products.api import serializers
from products import models
from rest_framework import status
from rest_framework.response import Response
import json

class ProductsViewSet(viewsets.ModelViewSet):
	serializer_class = serializers.ProductsSerializer
	queryset = models.Products.objects.all()

class CustomersViewSet(viewsets.ModelViewSet):
	serializer_class = serializers.CustomersSerializer
	queryset = models.Customers.objects.all()

	def create(self, request, *args, **kwargs):
		if (len(request.data['favorites']) > models.Customers.MAX_FAVORITES):
			return Response('Número máximo de favoritos excedido', status=status.HTTP_400_BAD_REQUEST)

		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		headers = self.get_success_headers(serializer.data)
		return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

	def update(self, request, *args, **kwargs):
		if (len(json.loads(json.dumps(dict(request.data)))['favorites']) > models.Customers.MAX_FAVORITES):
			return Response('Número máximo de favoritos excedido', status=status.HTTP_400_BAD_REQUEST)

		partial = kwargs.pop('partial', False)
		instance = self.get_object()
		serializer = self.get_serializer(instance, data=request.data, partial=partial)
		serializer.is_valid(raise_exception=True)
		self.perform_update(serializer)

		if getattr(instance, '_prefetched_objects_cache', None):
			instance._prefetched_objects_cache = {}

		return Response(serializer.data)