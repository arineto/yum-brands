from django.db import models


BRANDS = (
		(1, 'KFC'),
		(2, 'Taco Bell'),
		(3, 'PIzza Hut'),
	)


class Branch(models.Model):
	name = models.CharField(max_length=100, verbose_name="Company Name")
	franchise = models.IntegerField(max_length=1, choices=BRANDS, verbose_name="Brand")
	contact_name = models.CharField(max_length=100, verbose_name="Contact Name")
	phone = models.CharField(max_length=15, verbose_name="Phone Number")
	email = models.EmailField(verbose_name="Email")
	owner_name = models.CharField(max_length=100, verbose_name="Owner Name")
	operator_name = models.CharField(max_length=100, verbose_name="Operator Name")
	address = models.CharField(max_length=150, verbose_name="Address")
	latitude = models.CharField(max_length=50, verbose_name="Latitude", blank=True, null=True)
	longitude = models.CharField(max_length=50, verbose_name="Longitude", blank=True, null=True)
	date = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.name


class Brand(models.Model):
	name = models.CharField(max_length=50, verbose_name="Brand")
	icon = models.ImageField(upload_to="competitors_icons/", verbose_name="Icon")
	date = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.name


class Competitor(models.Model):
	name = models.CharField(max_length=50, verbose_name="Competitor")
	icon = models.ImageField(upload_to="competitors_icons/", verbose_name="Icon")
	date = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.name
