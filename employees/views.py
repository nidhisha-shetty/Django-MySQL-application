from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import Emp
from .forms import EmpForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def records_view(request):
    emp=Emp.objects.all()#.order_by("-emp_id") 
    paginator = Paginator(emp, 3) # Show 2 records per page.
    page_number = request.GET.get('page')
    try:
        emp =paginator.page(page_number)
    except PageNotAnInteger:
        emp = paginator.page(1)
    except EmptyPage:
        emp=paginator.page(paginator.num_pages)
    context={
        'emp':emp
    }
    return render(request, "record.html", context)

def search_view(request):
    query=request.GET.get('search')
    emp=Emp.objects.filter(emp_name__icontains=query)
    context={
        'emp':emp
    }
    return render(request, 'search.html', context)

def sort_view(request):
    emp=Emp.objects.all().order_by('emp_name')
    context={
        'emp':emp
    }
    return render(request, 'sort.html', context)

def create_view(request):
    form=EmpForm(request.POST or None)
    if form.is_valid():
        messages.info(request, "Employee added!")
        form.save()
        form=EmpForm()
    context={
		'Form':form
	}
    return render(request, "emp_create.html", context)

def edit_view(request):
    emp=Emp.objects.all()
    context={
        'emp':emp
    }
    return render(request, "emp_edit.html", context)

def delete_view(request):
    emp=Emp.objects.all()
    context={
        'emp':emp
    }
    return render(request, "emp_delete.html", context)

def edit_emp_view(request, id):
	obj=Emp.objects.get(id=id)
	form=EmpForm(request.POST or None, request.FILES or None, instance=obj)
	if form.is_valid():
		form.save()
		messages.info(request, "Employee details changed!")
		form=EmpForm()
	context={
	'context_form': form
	}
	return render(request, 'emp_detail_edit.html', context)

def delete_emp_view(request, id):
    obj=get_object_or_404(Emp, id=id)
    if request.method=='POST':
        obj.delete()
        return redirect("/emp_delete/")
        messages.info(request, "Employee details deleted!")
    context={
    'context_obj': obj
    }
    return render(request, 'emp_detail_delete.html', context)