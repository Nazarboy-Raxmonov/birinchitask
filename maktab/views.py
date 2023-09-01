from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import students, teachers
from .serializers import StudentsSerializers, TeachersSerializers
# Create your views here.

def studentdetailmodels(request,st_name):
    studentlist = get_object_or_404(students, ism = st_name)

    info = StudentsSerializers(studentlist)
    
    return JsonResponse(info.data, safe=False)

def studentsall(request):
    all_data = students.objects.all()
    result = StudentsSerializers(all_data, many = True)
    return JsonResponse(result.data, safe=False)

def teacherdetailmodels(request,teacher_id):
    teachermodels =get_object_or_404(teachers,id = teacher_id)

    info = TeachersSerializers(teachermodels)

    return JsonResponse(info.data,safe=False)

def teachersall(request):
    hammasi = teachers.objects.all()
    natija = TeachersSerializers(hammasi, many = True)

    return JsonResponse(natija.data,safe = False)