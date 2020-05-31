from django.db import models

class Product(models.Model):
	cost = models.IntegerField()
	dimension = models.DecimalField(max_digits=10, decimal_places=2)

	def __str__(self):
		return "Dimension (in inches): " + str(self.dimension)
