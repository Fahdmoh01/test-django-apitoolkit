from django.contrib.auth.models import BaseUserManager


class AccountManager(BaseUserManager):
    '''manages User account creation'''

    def create_user(self,email, password, name='-', age=0, role='DEFAULT-USER', **kwargs):
        user = self.model(email=email, password=password, name=name,age=age, role=role, **kwargs)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, name='-',age=0, role='DEFAULT-USER', **kwargs):
        user = self.create_user(email, password, name, age, role, **kwargs) 
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user