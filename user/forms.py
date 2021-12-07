from django.contrib.auth.models import User
from django.forms import ModelForm, PasswordInput, EmailInput, TextInput


class SignupForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name']
        widgets = {
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'ID로 사용할 이메일 주소를 입력해 주세요.'}),
            'password': PasswordInput(
                attrs={'class': 'form-control', 'minlength': 5, 'maxlength': 15,
                       'placeholder': '최소 5자, 최대 15 이내로 입력 가능합니다.'}),
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': '당신의 성을 입력해 주세요'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': '당신의 이름을 입력해 주세요'})
        }
        labels = {
            'email': 'email',
            'password': 'password',
            'first_name': 'first_name',
            'last_name': 'last_name'
        }


class SigninForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
        widgets = {
            'email': EmailInput(attrs={'class': 'form-control'}),
            'password': PasswordInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'email': 'email',
            'password': 'password'
        }
