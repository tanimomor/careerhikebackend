from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.managers import CustomUserManager


class CustomUser(AbstractBaseUser):
    USER_TYPE_CHOICES = (
        ('tutor', 'Tutor'),
        ('parent', 'Parent'),
        ('admin', 'Admin'),
        ('staff', 'Staff'),
    )
    email = models.EmailField(_('email address'), unique=True, null=True, blank=True)  # Allow null or blank email
    phone_number = models.CharField(
        max_length=11,  # 2 digits for '01' + 9 digits = 11 digits total
        unique=True,
        null=True,
        blank=True,
        validators=[
            RegexValidator(r'^01\d{9}$', _('Enter a valid phone number starting with 01 and followed by 9 digits.'))],
    )

    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'  # Can still use email as the default login field
    REQUIRED_FIELDS = []  # No other required fields (we'll handle this in the manager)

    def has_perm(self, perm, obj=None):
        # Admin users have all permissions
        if self.user_type == 'admin':
            return True

    def has_module_perms(self, app_label):
        # Admins can view all apps
        if self.user_type == 'admin':
            return True

    def __str__(self):
        return self.email or self.phone_number  # Display either email or phone number
