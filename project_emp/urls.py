"""project_emp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from employees.views import records_view, search_view, sort_view, create_view, edit_view, delete_view, edit_emp_view, delete_emp_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('records/', records_view),
    path('search/', search_view),
    path('sort/', sort_view),

    path('emp_create/', create_view),
    path('emp_edit/', edit_view),
    path('emp_delete/', delete_view),

    path('edit/<int:id>/', edit_emp_view),
    path('delete/<int:id>/', delete_emp_view),
]
