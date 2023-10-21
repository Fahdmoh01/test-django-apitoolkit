from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from . manager import AccountManager
# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    name  = models.CharField(max_length=80)
    age = models.IntegerField()
    email = models.EmailField(max_length=100, unique=True)
    role = models.CharField(max_length=100, blank=True, null=True)


    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at= models.DateTimeField(auto_now_add=True)

    # groups = models.ManyToManyField(Group, related_name='test_model_groups')

    objects= AccountManager() 

    def is_admin(self):
        '''check if user is tester'''
        return self.role == "TESTER"
    
    def get_fullname(self):
        '''returns the name of the user'''   
        return self.name if self.name else self.email if self.email else 'Anonymous' #noqa

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.get_fullname()
    
    class Meta:
        db_table = 'user'
