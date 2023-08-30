from django.db import models

# Create your models here.

class students(models.Model):
    ism = models.TextField(max_length=25)
    familiya = models.TextField(max_length=25)
    sinf = models.SmallIntegerField()

    def __str__(self) -> str:
        return self.ism
    class meta:
        db_table = 'students'


class teachers(models.Model):
    ism = models.TextField(max_length=25)
    familiya = models.TextField(max_length=25)
    fan = models.TextField()

    def __str__(self) -> str:
        return self.ism
    class Meta:
        db_table = 'teachers'