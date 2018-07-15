from django.db import models
from django.utils import timezone


class Data(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	location = models.CharField(max_length=200)
	sub_location = models.CharField(max_length=200)
	lon = models.DecimalField(max_digits=9, decimal_places=6)
	lat = models.DecimalField(max_digits=9, decimal_places=6)
	status = models.CharField(max_length=200)
	shop_name = models.CharField(max_length=200)
	owner_name = models.CharField(max_length=200)
	Enter_date = models.DateTimeField(
            blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.location