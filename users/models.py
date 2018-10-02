from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, BaseUserManager
from django.db.models import Model
from model_utils import Choices


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email=None, password=None):
        """
        Creates and saves a User with the given email, date of birth and password.
        :param email:
        :param password:
        :return:
        """
        if not email:
            raise ValueError('User must have an email address')
        if not password:
            raise  ValueError('User must have a password')

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email, date of birth and password.
        :param email:
        :param password:
        :return:
        """
        user = self.create_user(email,
                                password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    ROLE_TYPES = Choices((0, 'CUSTOMER'),
                         (1, 'Dealer-Sales Agent'),
                         (2, 'Dealer-Manager'),
                         (3, 'Dealer-Admin'),
                         (4, 'Global Administrator'))
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    username = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    address1 = models.CharField(max_length=512, blank=True, null=True)
    address2 = models.CharField(max_length=512, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    role = models.IntegerField(choices=ROLE_TYPES, default=0)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        db_table = 'auth_user'

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin

    @property
    def is_superuser(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self
