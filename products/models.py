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