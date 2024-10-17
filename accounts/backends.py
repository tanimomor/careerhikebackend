from django.contrib.auth.backends import ModelBackend
from accounts.models import CustomUser

class EmailOrPhoneBackend(ModelBackend):
    """
    Custom authentication backend that allows login with either email or phone number.
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        user = None
        if '@' in username:
            # Try to authenticate using email
            user = CustomUser.objects.filter(email=username).first()
        else:
            # Try to authenticate using phone number
            user = CustomUser.objects.filter(phone_number=username).first()

        if user and user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None