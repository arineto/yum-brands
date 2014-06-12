from django.db import models


BRANDS = (
		(1, 'KFC'),
		(2, 'Taco Bell'),
		(3, 'PIzza Hut'),
	)


class Branch(models.Model):
	brand = models.IntegerField(max_length=1, choices=BRANDS, verbose_name="Brand")
	address = models.CharField(max_length=150, verbose_name="Address")
	date = models.DateTimeField(auto_now=True)
