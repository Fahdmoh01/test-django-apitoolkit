from django.db import models

# Create your models here.

class TestModel(models.Model):
    name  = models.CharField(max_length=80)
    age = models.IntegerField()
    email = models.EmailField()
    role = models.CharField(max_length=100, blank=True, null=True)


    def is_admin(self):
        '''check if user is tester'''
        return self.role == "TESTER"
