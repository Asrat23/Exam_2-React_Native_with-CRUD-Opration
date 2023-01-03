from django.db import models
 
# Create your models here.
        #  student
class student(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    grade=models.CharField(max_length=30, null=True )
    def __str__(self):
        return self.fname

