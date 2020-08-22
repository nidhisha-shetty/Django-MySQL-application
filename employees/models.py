from django.db import models

# Create your models here.
class Emp(models.Model):
	emp_name = models.CharField(max_length=100, null=False);
	emp_id = models.IntegerField(null=False);
	emp_salary = models.BigIntegerField(null=False);

	def go_to_link_edit(self):
		return f"/edit/{self.id}/"

	def go_to_link_delete(self):
		return f"/delete/{self.id}"