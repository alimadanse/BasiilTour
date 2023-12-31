from django import forms
# from django.auth.models.User import User
from accounts.models import CustomUser

from .models import Tour,TourRegistration

class TourForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = ('title', 'description', 'photo')

class TourRegisterForm(forms.ModelForm):
    class Meta:
        model = TourRegistration
        fields = ('first_name', 'last_name', 'nat_id', 'age', 'phone_number')
        labels = {
            'first_name' : 'نام', 
            'last_name':'نام خانوادگی',
            'nat_id':'کد ملی', 
            'age' : 'سن',
            'phone_number' : 'شماره تلفن',
        }