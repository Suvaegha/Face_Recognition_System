import base64
import io
import json

from django.core.files.images import ImageFile
from django.core.paginator import Paginator
from django.core.serializers import serialize
from django.db import IntegrityError, transaction
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import EmployeeDetails


def dashboard(request):
    return render(request, 'adminPanel/dashboard.html')


def register_employee(request):
    return render(request, 'adminPanel/register_employee.html', {'title': 'About'})


def employees(request):
    return render(request, 'adminPanel/employee_list.html')


@csrf_exempt
@transaction.atomic
def post_employee(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        try:
            emp_obj = EmployeeDetails.objects.create(emp_name=data['name'],
                                                     emp_email=data['email'],
                                                     emp_number=data['mobile'],
                                                     password=data['password'],
                                                     emp_designation=data['designation'],
                                                     emp_department=data['department'])

            image = ImageFile(io.BytesIO(base64.b64decode(data['image'])), name=f"emp_{emp_obj.id}.jpeg")
            emp_obj.image = image
            emp_obj.save()

        except IntegrityError as e:
            # Handle integrity errors (e.g., unique constraint violation)
            print("Integrity error:", e)
        except Exception as e:
            # Handle any other unexpected errors
            print("An unexpected error occurred:", e)

    return JsonResponse({'message': 'success'})


def employee_list(request):
    employees = EmployeeDetails.objects.all()

    paginator = Paginator(employees, 1)
    page_number = request.GET.get('page')
    print('page:', page_number)
    employees = paginator.get_page(page_number)

    # Serialize the paginated queryset
    serialized_employees = [
        {'id': employee.id, 'name': employee.emp_name, 'email': employee.emp_email, 'mobile': employee.emp_number,
         'designation': employee.emp_designation, 'department': employee.emp_department,
         'image': base64.b64encode(employee.image).decode('utf-8')} for
        employee in employees
    ]

    return JsonResponse({'employees': serialized_employees, 'total_pages': paginator.num_pages, 'page': page_number})
