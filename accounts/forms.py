from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CusomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username' ,'email', )
        
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser 
        fields = UserChangeForm.Meta.fields 
        