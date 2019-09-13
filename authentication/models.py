import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator


# Create your models here.

class AccountValidator(UnicodeUsernameValidator):
    regex = r'^[\w.@+-\s]+$'


class AccountManager(BaseUserManager):
    def create_user(self, password=None, **kwargs):
        user = self.model(
            username=kwargs.get('username'),
            phone_number=kwargs.get('phone_number'),
            email=kwargs.get('email'),
            user_uuid=uuid.uuid4(),
        )
        user.set_password(password)
        user.save()

        # TODO : Possibly create user wallet here
        return user

    def create_attendant(self, password=None, **kwargs):
        user = self.model(
            username=kwargs.get('username'),
            phone_number=kwargs.get('phone_number'),
            email=kwargs.get('email'),
            user_uuid=uuid.uuid4(),
        )
        user.is_attendant = True
        user.set_password(password)
        user.save()

        # TODO : Possibly create user wallet here
        return user

    def create_superuser(self, password, **kwargs):
        user = self.create_user(password,
                                   username=kwargs.get('username'),
                                   phone_number=kwargs.get('phone_number'),
                                   email=kwargs.get('email'),
                                   user_uuid=uuid.uuid4(),
                                   )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(max_length=15, unique=True, null=True)
    email = models.EmailField(('email'), max_length=254, unique=False, null=True)
    username = models.CharField(('username'), max_length=40, unique=True, null=True)
    title = models.CharField(('title'), max_length=40, unique=False, null=True, default='user')
    user_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    is_active = models.BooleanField(default=True, help_text=('Designates whether the user is active'))
    is_customer = models.BooleanField(default=False, help_text=('Designates whether the user is a customer'))
    is_attendant = models.BooleanField(default=False, help_text=('Designates whether the user is an attendant'))
    is_manager = models.BooleanField(default=False, help_text=('Designates whether the user is a manager'))
    is_pigeon_staff = models.BooleanField(default=False, help_text=('Designates whether the user is a pigeon staff'))
    is_staff = models.BooleanField(default=False, help_text=('Designates whether the user can log onto the site'))

    date_joined = models.DateTimeField(('date joined'), auto_now_add=True)
    date_modified = models.DateTimeField(('date modified'), auto_now=True)

    objects = AccountManager()

    USERNAME_FIELD = 'username'

    username_validator = AccountValidator

    class Meta:
        verbose_name = ('user')
        verbose_name_plural = ('users')

    def get_full_name(self):
        return  "{} {}".format(self.username, self.phone_number)

    def get_short_name(self):
        return self.username

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.username)
