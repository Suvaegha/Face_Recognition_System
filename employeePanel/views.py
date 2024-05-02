import base64
import json

from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator
from django.core.serializers import serialize
from django.db import IntegrityError, transaction
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from adminPanel.models import EmployeeDetails


def dashboard(request):
    return render(request, 'employeePanel/dashboard.html')


def leave_request(request):
    return render(request, 'employeePanel/leave_request.html', {'title': 'About'})


def leave_report(request):
    return render(request, 'employeePanel/leave_report.html', {'title': 'About'})


def post_leave_request(request):
    if request.method == 'POST':
        employee = EmployeeDetails.objects.get(
            id=request.POST.get('employee_id')
        )

        return JsonResponse({'success': 'Successfully posted leave request'}, 201)


def login(request):
    return render(request, 'employeePanel/login.html')


@csrf_exempt
def post_login(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        email = json_data.get('email')
        password = json_data.get('password')
        print(email, password)
        try:
            user = EmployeeDetails.objects.get(emp_email=email)
            print(user)
            if user.password == password:
                request.session['employee_id'] = user.id
                request.session['employee_name'] = user.emp_name
                return redirect('employee-dashboard')
                # return JsonResponse({'success': 'Successfully'})
            else:
                # Handle invalid login credentials
                return render(request, 'employeePanel/login.html', {'error': 'Invalid username or password.'})
        except EmployeeDetails.DoesNotExist:
            print('Invalid username or password.')
            return JsonResponse({'failure': 'Invalid username or User not registered'}, status=400)

    else:
        return render(request, 'employeePanel/login.html')
