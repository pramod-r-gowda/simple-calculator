from django.db import models

# Create your models here.
class Calculate(models.Model):
	n1=models.CharField(max_length=200,null=True)
	n2=models.CharField(max_length=200,null=True)
