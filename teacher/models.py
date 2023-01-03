from django.db import models

# Create your models here.
    # teacher
class teacher(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    salary=models.CharField(max_length=30, )
    def __str__(self):
        return self.fname  