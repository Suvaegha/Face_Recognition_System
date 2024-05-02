from django.db import models


# Create your models here.
class EmployeeAttendance(models.Model):
    emp_name = models.CharField(max_length=50)
    attendance_type = models.CharField(max_length=15)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return self.emp_name

    class Meta:
        db_table = 'employee_attendance'
