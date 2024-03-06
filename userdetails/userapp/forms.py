from django import forms
from django.contrib.auth.models import User
from userapp.models import userdata
from django_recaptcha.fields import ReCaptchaField
class userForms(forms.ModelForm):
    password=forms.CharField(max_length=20,required=True,widget=forms.PasswordInput)
    class Meta: 
        model=User
        fields=['username','email','password']
class userprofile(forms.ModelForm):
    class Meta:
        model=userdata
        fields=['address','phone','img']
    captcha = ReCaptchaField()

class user_updatef(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email']