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

		def validate_name(self, value):
			# print(data)
			# sys.exit()
			if 'django' not in value.lower():
				raise serializers.ValidationError("Blog post is not about Django")
			return value