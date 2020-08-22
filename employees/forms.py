from django import forms
from .models import Emp
class EmpForm(forms.ModelForm):
	class Meta:
		model = Emp
		fields=[
			'emp_id',
			'emp_name',
			'emp_salary'
		]
