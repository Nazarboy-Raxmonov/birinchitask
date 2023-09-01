from rest_framework import serializers
from .models import students, teachers

class StudentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = students
        fields = ('ism','familiya','sinf')

class TeachersSerializers(serializers.ModelSerializer):
    class Meta:
        model = teachers
        fields = ('ism','familiya','fan')

