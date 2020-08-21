from django.shortcuts import render
from .models import Emp
# Create your views here.

def records_view(request):
    emp=Emp.objects.all()
    context={
        'emp':emp
    }
    return render(request, "record.html", context)
