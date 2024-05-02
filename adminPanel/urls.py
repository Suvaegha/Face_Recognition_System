from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='admin-dashboard'),
    path('register_employee/', views.register_employee, name='register-employee'),
    path('post_employee/', views.post_employee, name='post-employee'),
    path('employee_list/', views.employee_list, name='employee-list'),
    path('employees/',views.employees, name='employees')
]