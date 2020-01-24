from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(UserCreationForm):
    dob = forms.DateField(help_text="Required format: YYYY/MM/DD")
    class Meta:
        model  = User
        fields ={ 
            'username',
            'dob',
            'password1',
            'password2'
        }
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label= 'Display Name'
        # self.fields['email'].label = 'Email Address'


