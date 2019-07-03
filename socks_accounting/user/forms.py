from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.hashers import make_password



class ProfileForm(forms.ModelForm):
    username = forms.CharField(max_length=155, label='نام کاربری')
    first_name = forms.CharField(max_length=155, label='نام')
    last_name = forms.CharField(max_length=155, label='نام خانوادگی')
    email = forms.EmailField(max_length=155, label='ایمیل')
    password = forms.CharField(widget=forms.PasswordInput, label='رمزعبور')
    re_password = forms.CharField(widget=forms.PasswordInput, label='تکرار رمزرعبور')
    def clean(self):
        data = self.cleaned_data
        print(self.cleaned_data)
        pass1 = data.get('password')
        pass2 = data.get('re_password')
        if pass1 != pass2:
            raise forms.ValidationError('رمز عبور یکسان نیست')
        return data 

    class Meta:
        model = Profile
        exclude = ('user',)
        


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'