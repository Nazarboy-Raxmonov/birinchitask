from django.urls import path
from .views import studentdetailmodels, studentsall,teacherdetailmodels,teachersall


urlpatterns = [
    path('studentsdetails/<str:st_name>',studentdetailmodels),
    path('studentsall/',studentsall),
    path('teachersdetail/<int:teacher_id>',teacherdetailmodels),
    path('teachersall/', teachersall)
]
