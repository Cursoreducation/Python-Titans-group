from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.backends import ModelBackend


class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user = User.objects.filter(Q(username=username) | Q(email=username)).first()
        if user and user.check_password(password):
            return user
        return None