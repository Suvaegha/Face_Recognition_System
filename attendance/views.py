import base64
import io
import json
import os
from datetime import datetime

import face_recognition
from django.core.files.storage import default_storage

from attendance.models import EmployeeAttendance
from django.core.files.images import ImageFile
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from adminPanel.models import EmployeeDetails


def capture_attendance(request):
    return render(request, 'attendance/attendance.html')


# Create your views here.
@csrf_exempt
def attendance(request):
    obj = EmployeeDetails.objects.all()
    data = json.loads(request.body)

    ##################### Image handling ###################
    imageFile = ImageFile(io.BytesIO(base64.b64decode(data['image'])), name="emp_img.jpeg")
    file_path = "image2/"
    os.makedirs(file_path, exist_ok=True)
    # Create a new file path
    file_path = os.path.join(file_path, "emp_img.jpeg")
    # Write the uploaded image file to the filesystem
    with open(file_path, 'wb') as f:
        # for chunk in io.BytesIO(base64.b64decode(data['image'])).chunks():
        f.write(base64.b64decode(data['image']))
    ############################################################

    print(imageFile)
    for i in obj:
        img = str(i.image)
        emp_id = i.id
        status = check(img, imageFile, emp_id)
        if status:
            return HttpResponse("success")
    return HttpResponse("Failed")


@csrf_exempt
def check(image, data, emp_id):
    now = datetime.now()
    current_date = now.date()

    harsh_image = face_recognition.load_image_file("./" + image)
    harsh_face_encoding = face_recognition.face_encodings(harsh_image)[0]

    kunal_image = face_recognition.load_image_file(data)
    kunal_face_encoding = face_recognition.face_encodings(kunal_image)[0]

    results = face_recognition.compare_faces([harsh_face_encoding], kunal_face_encoding)

    if results[0]:
        print(results)
        # while results[0]:
        #     id = emp_id
        #
        #     if EmployeeAttendance.objects.filter(
        #             Q(fk_Employee_user_id=id) & Q(check_out_Created_date_time_date=current_date) & (
        #                     Q(Attendance_Type="Check-out"))).exists() and EmployeeAttendance.objects.filter(
        #         fk_Employee_user_id=id).last().Attendance_Туре == "Check-out":
        #         obj = EmployeeAttendance.objects.get(
        #             Q(fk_Employee_user_id=id) & Q(check_In_Created_date_time_date=current_date) & (
        #                 Q(Attendance_Туре="Check-out"))).id
        #         # print (obj,'----------obj')
        #         obj_emp = EmployeeAttendance.objects.get(id=obj)
        #         obj_emp.Attendance_Type = "Check-in"
        #         obj_emp.IP_Address = 'ip-address'
        #         obj_emp.check_In_Created_date_time = now
        #         obj_emp.save()
        #
        #         print("Face Recognized Successfully")
        #         return HttpResponse("success")
        #
        #     elif EmployeeAttendance.objects.filter(
        #             Q(fk_Employee_user_id=id) & Q(check_In_Created_date_time_date=current_date) & (
        #                     Q(Attendance_Type="Check-in"))).exists() and EmployeeAttendance.objects.filter(
        #         fk_Employee_user_id=id).last().Attendance_Туре == "Check-in":
        #         obj = EmployeeAttendance.objects.get(
        #             Q(fk_Employee_user_id=id) & Q(check_In_Created_date_time_date=current_date) & (
        #                 Q(Attendance_Type="Check-in"))).id
        #         #   print(ob],
        #         obj_emp = EmployeeAttendance.objects.get(id=obj)
        #         obj_emp.Attendance_Type = "Check-out"
        #         obj_emp.IP_Address = 'ip-address'
        #         obj_emp.check_In_Created_date_time = now
        #         obj_emp.save()
        #         print('Face Recognised Successfully')
        #         return HttpResponse("Success")
        #
        #     else:
        #         EmployeeAttendance.objects.create(fk_Employee_user_id=id, Attendance_Type="Check-in",
        #                                           IP_Address='ip-address', check_In_Created_date_time=now)
        #         print('Face Recognised Successfully')
        #         return True
    else:
        return False
