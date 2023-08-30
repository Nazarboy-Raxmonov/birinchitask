from .models import students, teachers
from django.urls import path
from .views import studentdetailmodels, studentsall,teacherdetailmodels,teachersall


urlspatterns = [
    path('students/details/<str:st_name>',studentdetailmodels),
    path('students/all/',studentsall),
    path('teachers/detail/<int:teacher_id>',teacherdetailmodels),
    path('teachers/all/', teachersall)
]