from django.db import models

# Create your models here.

class User(models.Model):
    first_name=models.TextField()
    last_name=models.TextField()
    user_name=models.TextField()
    email=models.EmailField()
    password=models.TextField()

    def __str__(self):
        return self.first_name+" "+self.last_name