from rest_framework import serializers
from products import models

class ProductsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.Products
		fields = '__all__'

class CustomersSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.Customers
		fields = ('id', 'email', 'name', 'favorites')