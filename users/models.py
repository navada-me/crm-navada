from django.db import models

# Create your models here.
class Customer(models.Model):
	first_name = models.CharField(max_length=50, null=True)
	last_name = models.CharField(max_length=50, null=True)
	email = models.EmailField(null=True)
	phone = models.IntegerField(null=True)
	date_created  = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.first_name

class Tag(models.Model):
	name = models.CharField(max_length=50, null=True)

	def __str__(self):
		return self.name


class Product(models.Model):
	CATEGORY = (
		('Cat 1 ', 'Cat 1 '),
		('Cat 2 ', 'Cat 2 '),
		('Cat 3 ', 'Cat 3 '),
		)
	name = models.CharField(max_length=200, null=True)
	description = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
	category = models.CharField(max_length = 200, null=True, choices=CATEGORY)
	date_created  = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.name


class Order(models.Model):
	STATUS = (
		('Pending', 'Pending'),
		('Shipped', 'Shipped'),
		('Delivered', 'Delivered'),
		)
	customer = models.ForeignKey(Customer, on_delete = models.SET_NULL, null=True)
	product = models.ForeignKey(Product, on_delete = models.SET_NULL, null=True)
	status = models.CharField(max_length = 200, null=True, choices=STATUS)
	date_created  = models.DateTimeField(auto_now_add=True)
	tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.status