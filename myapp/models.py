from django.db import models

# Create your models here.


class Contact(models.Model):
     name = models.CharField(max_length=122)
     email = models.CharField(max_length=122)
     phone = models.CharField(max_length=12)
     address = models.TextField()
     date = models.DateField()

     def __str__(self):
       return self.name

class detail(models.Model):
     title=models.CharField(max_length=122)
     image=models.ImageField(upload_to="static")
   
     def __str__(self):
       return self.title