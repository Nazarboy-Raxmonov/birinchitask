from django.db import models

# Create your models here.

class students(models.Model):
    ism = models.TextField(max_length=25)
    familiya = models.TextField(max_length=25)
    sinf = models.SmallIntegerField()

    class meta:
        db_name = 'students'


class teachers(models.Model):
    ism = models.TextField(max_length=25)
    familiya = models.TextField(max_length=25)
    fan = models.TextField()

    class Meta:
        db_name = 'teachers'