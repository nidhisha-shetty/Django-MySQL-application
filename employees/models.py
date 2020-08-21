from django.db import models

# Create your models here.
class Emp(models.Model):
	emp_name = models.TextField(max_length=100, null=False);
	emp_id = models.IntegerField(null=False);
	emp_sal = models.IntegerField(null=False);