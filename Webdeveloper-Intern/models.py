from django.db import models

class Dreamreal(models.Model):

   Serial_id = models.AutoField()
   mail = models.CharField(max_length = 50)
   name = models.CharField(max_length = 50)
   phonenumber = models.IntegerField()
   Current_location=models.CharField(max_length = 50)
   Experience=models.IntegerField(max_length = 50)
   skills = models.TextField(max_length=1000, help_text="Enter a brief description of your skills")
   class Meta:
      db_table = "dream_real"
