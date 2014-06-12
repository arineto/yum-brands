from django.db import models


BRANDS = (
		(1, 'KFC'),
		(2, 'Taco Bell'),
		(3, 'PIzza Hut'),
	)


class Branch(models.Model):
	brand = models.IntegerField(max_length=1, choices=BRANDS, verbose_name="Brand")
	address = models.CharField(max_length=150, verbose_name="Address")
	latitude = models.CharField(max_length=50, verbose_name="Latitude", blank=True, null=True)
	longitude = models.CharField(max_length=50, verbose_name="Longitude", blank=True, null=True)
	date = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.get_brand_display()
