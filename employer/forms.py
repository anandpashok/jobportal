from django import forms
from employer.models import Jobs
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class JobForm(forms.ModelForm):
   class Meta:
       model=Jobs
       fields="__all__"


class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email","password1","password2","username"]


class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())


# same form as model



# from employer.models import Jobs
#
# class JobForm(forms.ModelForm):
#     class Meta:
#         model=Jobs
#         fields="__all__"