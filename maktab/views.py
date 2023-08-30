from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import students, teachers
# Create your views here.

def studentdetailmodels(request,st_name):
    studentlist = students.objects.get_object_or_404(ism = st_name)

    info = {
        "name" : studentlist.ism,
        "surname" : studentlist.familiya,
        "grade" : studentlist.sinf 
        }
    
    return JsonResponse(info, safe=false)

def studentsall(request):
    result = []
    all_data = students.objects.all()
    for i in all_data:
        result.append({
        'name' : i.ism,
        'surname' : i.familiya,
        'grade' : i.sinf
        })
    return JsonResponse(result, safe=false)

def teacherdetailmodels(request,teacher_id):
    teachermodels = teachers.objects.get_object_or_404(id = teacher_id)

    info = {
        'name' : teachermodels.ism,
        'surname' : teachermodels.familiya,
        'subject' : teachermodels.fan
    }

    return JsonResponse(info,safe=false)

def teachersall(request):
    natija = []
    hammasi = teachers.objects.all()
    for i in hammasi:
        natija.append({
        'name' : teachermodels.ism,
        'surname' : teachermodels.familiya,
        'subject' : teachermodels.fan
        })

    return JsonResponse(natija,safe = false)