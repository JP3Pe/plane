from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, PasswordInput


class SignupForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': TextInput(attrs={'class': 'form-control', 'maxlength': 15, 'placeholder': '15자 이내로 입력 가능합니다.'}),
            'password': PasswordInput(
                attrs={'class': 'form-control', 'minlength': 5, 'maxlength': 15,
                       'placeholder': '최소 5자, 최대 15 이내로 입력 가능합니다.'}),
        }
        labels = {
            'username': 'username',
            'password': 'password'
        }


class SigninForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': TextInput(attrs={'class': 'form-control'}),
            'password': PasswordInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'username': 'username',
            'password': 'password'
        }
