from django.db import models
from jsonfield import JSONField

# Create your models here.
class EnterData(models.Model):
    first_name = models.CharField(max_length=50,blank=True)
    last_name = models.CharField(max_length=50,blank=True)
    university_name =models.CharField(max_length=200,blank=True)
    class_10_percent = models.IntegerField(blank=True,default=0)
    class_12_percent = models.IntegerField(blank=True,default=0)
    bachelors_percent = models.IntegerField(blank=True,default=0)
    work_exp = models.CharField(max_length=200)
    german_grade = models.CharField(max_length=20,verbose_name="German Grade (For eg: A1,A2,etc)")
    semester = models.CharField(max_length=200,blank = True)
    hints = JSONField(default=[],blank = True)


class HintsData(models.Model):

    hint1 = models.CharField(max_length=200,blank = True)
    hint2 = models.CharField(max_length=200,blank = True)
    hint3 = models.CharField(max_length=200,blank = True)
