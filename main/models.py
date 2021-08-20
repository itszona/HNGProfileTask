from django.db import models

# Create your models here.

class Response(models.Model):
	name = models.CharField(max_length=30)
	email = models.EmailField()
	response = models.TextField()

	def __str__(self):
		return self.name