from django.db import models


# Create your models here.

class EmployeeDetails(models.Model):
    emp_name = models.CharField(max_length=50)
    emp_email = models.EmailField()
    emp_number = models.CharField(max_length=10, unique=True)
    emp_designation = models.CharField(max_length=30)
    emp_department = models.CharField(max_length=20)
    password = models.CharField(max_length=30, default="root")
    image = models.ImageField(upload_to='media/registered_employees/')

    def __str__(self):
        return self.emp_name

    class Meta:
        db_table = 'employee_details'

    # def get_absolute_url(self):
    #     return reverse('post-detail', kwargs={'pk': self.pk})


class LeaveDetails(models.Model):
    emp_id = models.ForeignKey(EmployeeDetails, to_field='id', on_delete=models.CASCADE)
    emp_name = models.CharField(max_length=50)
    leave_date = models.DateField()
    leave_reason = models.TextField()
    status = models.CharField(max_length=10)

    def __str__(self):
        return self.emp_name

    class Meta:
        db_table = 'leave_details'
