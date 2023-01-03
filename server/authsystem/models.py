import uuid

from django.db import models
from django.urls import reverse_lazy
from django.contrib.auth.models import (
	AbstractBaseUser, BaseUserManager,
)

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(email=self.normalize_email(email))
        user.username = username
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.private_access = True
        user.save()

        return user

class User(AbstractBaseUser):
    id = models.UUIDField(
        primary_key=True,
        db_index=True,
        default=uuid.uuid4,
        editable=False)
    email = models.EmailField(max_length=256, unique=True)
    username = models.CharField(max_length=256, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # Auth settings
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [
        'email'
    ]

    objects = UserManager()

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    def __str__(self):
        return self.email

    def get_absolute_url(self,):
        return reverse_lazy('moder_user_detail', kwargs={'id': self.id})

    class Meta:
        indexes = [
            models.Index(fields=['id'], name='id_index'),
        ]

