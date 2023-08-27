from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


class AccountManager(BaseUserManager):
    def create_user(self, phone, password=None, **extra_fields):
        if not phone:
            raise TypeError('Phone not')
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        if not password:
            raise TypeError('password no')
        user = self.create_user(phone, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    ROLE = (
        (1, 'Daraxt ektiruvchi'),
        (2, 'Daraxt ekuvchi')
    )
    phone = models.CharField(max_length=14, unique=True, db_index=True)
    image = models.ImageField(null=True, blank=True, upload_to='accounts/')
    role = models.IntegerField(choices=ROLE, default=1)
    bio = models.TextField(null=True, blank=True)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_login = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)

    objects = AccountManager()
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.phone}'


class VerifyPhone(models.Model):
    class Meta:
        verbose_name = _("Telefon raqamni tasdiqlash")
        verbose_name_plural = _("Telefon raqam tasdiqlash")

    phone = models.CharField(max_length=15, verbose_name=_("Phone number"))
    code = models.CharField(max_length=10, verbose_name=_("Code"))

    def __str__(self):
        return self.phone
