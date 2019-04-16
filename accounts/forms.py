from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class CustomUserCreationFrom(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ['username','email']
        
class CustomUserChangeFrom(UserChangeForm):
    password = None 
    # UserChangeForm의 password 칼럼에 아무것도 안넣음
    
    class Meta:
        model = User
        fields = ['email','introduce','profile_image']