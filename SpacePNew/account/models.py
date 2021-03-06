from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def _create(self, email, password, name, **extra_fileds):
        if not email:
            raise ValueError('Email cannot be empty')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fileds)
        user.set_password(password)
        user.save()
        return user

    #создает обычных пользователей
    def create_user(self, email, password, name, **extra_fields):
        extra_fields.setdefault('is_active', False)
        extra_fields.setdefault('is_staff', False)
        return  self._create(email, password, name, **extra_fields)

    def create_superuser(self, email, password, name, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        return self._create(email, password, name, **extra_fields)


class User(AbstractBaseUser):
    email = models.EmailFiled(primary_key=True)
    name= models.CharField(max_length=30)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=8, blank=True)

    objects = UserManager()

    USERNAME_FILE = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

    def has_module_perms(self, app_label):
        return self.is_staff

    def has_perm(self, obj=None):
        return self.is.staff

