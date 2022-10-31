from django.db import models

# Create your models here.

class details(models.Model):
    username=models.CharField(max_length=30)
    age=models.IntegerField()
    Account_number=models.IntegerField()
    phone_number=models.IntegerField()
    email=models.EmailField(max_length=30)
    password_type=models.IntegerField()
    password=models.CharField(max_length=20)

    def __str__(self):
        return self.username

