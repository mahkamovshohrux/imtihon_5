from django.db import models
from datetime import datetime

# Create your models here.
class Yangilikmadel1(models.Model):
    txt_name1 = models.CharField(max_length=25,default="")
    date_time1 = models.DateTimeField(default=datetime.now)
    status1 = models.BooleanField(default=False)
    description1 = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.txt_name1
    class Meta:
        db_table = 'Yangilik1'

class Yangilikmadel2(models.Model):
    txt_name2 = models.CharField(max_length=25,default="")
    date_time2 = models.DateTimeField(default=datetime.now)
    status2 = models.BooleanField(default=False)
    description2 = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.txt_name2
    class Meta:
        db_table = 'Yangilik2'