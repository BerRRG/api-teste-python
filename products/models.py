from django.db import models
from uuid import uuid4
from django.core.validators import validate_email
from django.db.models.signals import m2m_changed
from django.core.exceptions import BadRequest
import sys

class Products(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
	title = models.CharField(max_length=255)
	image = models.CharField(max_length=255)
	brand = models.CharField(max_length=255)
	reviewScore = models.IntegerField()
	price = models.DecimalField(max_digits = 5,decimal_places = 2)

	def save(self, *args, **kwargs):
		print(self)
		raise ValueError("Updating the value of creator isn't allowed")		

	def __str__(self):
		return self.title


class Customers(models.Model):
	MAX_FAVORITES = 3

	id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
	email = models.CharField(max_length=255, unique=True, validators=[validate_email])
	name = models.CharField(max_length=255)
	favorites = models.ManyToManyField(Products)

	def __str__(self):
		return self.name

def favorites_changed(sender, instance, pk_set, **kwargs):
	allIds = []
	storedIds = instance.favorites.all()
	for i in storedIds:
		allIds.append(i.id)

	addedIds = pk_set
	for i in addedIds:
		allIds.append(i)

	if (len(allIds) > Customers.MAX_FAVORITES):
		raise BadRequest('Max number of favorites is 3.')

m2m_changed.connect(favorites_changed, sender=Customers.favorites.through)