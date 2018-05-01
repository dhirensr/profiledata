from django.db import models
from jsonfield import JSONField

# Create your models here.
class EnterData(models.Model):
    name = models.CharField(max_length=50,blank=True,\
                                  verbose_name='Your Name (only if you want to submit)')
    admit_unis = models.TextField(max_length=400,\
                                  verbose_name='Add all the Universities and course that you received ADMIT from')
    reject_unis = models.TextField(max_length=400,blank=True,\
                                   verbose_name='Add all the Universities and course that you received a REJECTION from')
    ms_stream = models.CharField(max_length=400,\
                                 verbose_name='MS Field (Which field are you studying in right now)')
    extra_curricular= models.TextField(max_length=400,blank=True,\
                                       verbose_name='Misc. (Some important extra curricular activities or anything that you think is important to have in the profile)')
    class_10_percent = models.IntegerField(default=0,verbose_name='10th Grade percent( Rounded off)')
    class_12_percent = models.IntegerField(default=0,\
                                           verbose_name='12th/Diploma Grade	12th/Diploma Grade	12th/Diploma Grade (Rounded off)')
    bachelors_percent = models.FloatField(default=0,\
                                            verbose_name='B.Tech. score ')
    bachelors_stream = models.CharField(max_length=100,default=0,\
                                        verbose_name='B.Tech. stream')
    toefl = models.IntegerField(default=0,\
                                verbose_name='TOEFL/IELTS')
    gre_score = models.IntegerField(blank=True,default=0,\
                                    verbose_name='GRE score')
    work_exp = models.IntegerField(default=0,blank=True,
                                   verbose_name='Work Experience ')
    german_grade = models.CharField(max_length=20,verbose_name="German Grade (For eg: A1,A2,etc)",\
                                    blank=True)
    semester = models.IntegerField(default=0,blank = True,\
                                   verbose_name='Semester (Meaning how many semesters have you studied till now.)')
    timestamp= models.DateTimeField(auto_now=True)


class HintsData(models.Model):

    hint1 = models.CharField(max_length=200,blank = True)
    hint2 = models.CharField(max_length=200,blank = True)
    hint3 = models.CharField(max_length=200,blank = True)
