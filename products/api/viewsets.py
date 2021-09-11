from rest_framework import viewsets
from products.api import serializers
from products import models

class ProductsViewSet(viewsets.ModelViewSet):
	serializer_class = serializers.ProductsSerializer
	queryset = models.Products.objects.all()

class CustomersViewSet(viewsets.ModelViewSet):
	serializer_class = serializers.CustomersSerializer
	queryset = models.Customers.objects.all()

	# def post(self, request, *args, **kwargs):
	# 	sys.exit()
	# 	serializer = MessagesSerializer(
	# 		data=request.data
	# 	)
	# 	if serializer.is_valid():
	# 		serializer.save()
	# 		return Response({'success': True})
	# 	else:
	# 		return Response(
	# 			serializer.errors,
	# 			status=status.HTTP_400_BAD_REQUEST
	# 		)