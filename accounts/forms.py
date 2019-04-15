from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationFrom(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ['username','email']