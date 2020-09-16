from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import AbstractUser,BaseUserManager,AbstractBaseUser

# Create your models here.
#TODO  



class MyUserManager(BaseUserManager):
    def create_user(self,email, password=None):
        user=self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self,email,password=None):
        admin=self.create_user(email=email,password=password)
        admin.is_admin=True
        admin.save(using=self._db)
        return admin

class User(AbstractUser):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    address=models.CharField(max_length=100)
    phone=PhoneField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    def __str__(self):
        return self.email
