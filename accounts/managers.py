from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, email=None, phone_number=None, password=None, **extra_fields):
        """
        Create and return a user with an email or phone number and password.
        """
        if not email and not phone_number:
            raise ValueError(_('The user must have either an email or a phone number'))

        if email:
            email = self.normalize_email(email)

        user = self.model(email=email, phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, phone_number=None, password=None, **extra_fields):
        """
        Create and return a superuser with either email or phone number and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(email=email, phone_number=phone_number, password=password, **extra_fields)

    def active_users(self):
        return self.filter(is_active=True)

    def tutors(self):
        return self.filter(user_type='tutor')

    def parents(self):
        return self.filter(user_type='parent')

    def staffs(self):
        return self.filter(user_type='staff')
