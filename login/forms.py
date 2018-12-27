from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=50, required=False, help_text="Optional")
    #email = forms.EmailField(max_length=254, help_text="Required")

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Username',
                    'required': 'required',
                    'autofocus': 'autofocus',
                    #'style': 'margin-bottom: 7px;'
                }
            ),
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter First Name',
                    #'style': 'margin-bottom: 7px;'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Last Name',
                    #'style': 'margin-bottom: 7px;'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Email',
                    'required': 'required',
                    #'style': 'margin-bottom: 7px;'
                }
            ),


        }

        def __init__(self, *args, **kwargs):
            super(SignUpForm, self).__init__(*args, **kwargs)
            #self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': _("Enter Password"),'class': 'form-control',})
            #self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': _("Enter Password"), 'class': 'form-control',})
