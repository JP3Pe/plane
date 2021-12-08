from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import SigninForm, SignupForm


def sign_up(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid:
            if User.objects.filter(email=form.cleaned_data['email']):
                messages.error(request, '해당 유저명은 이미 사용 중 입니다.')
                return redirect('sign-up')
            else:
                User.objects.create_user(**form.cleaned_data)
            return redirect('sign-in')
        else:
            return redirect('sign-up')

    else:
        form = SignupForm()
        return render(request, 'sign_up.html', {'form': form})


def sign_in(request):
    # if request.method == "POST":
    #     form = UserSigninForm(request.POST)
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     user = auth.authenticate(request, username=username, password=password)
    #
    #     # 로그인 성공인 경우
    #     if user is not None:
    #         auth.login(request, user)
    #         return redirect(bulletin_board_views.show_post)
    #     # 로그인 실패 시
    #     else:
    #         messages.error(request, '존재하지 않는 아이디 이거나 비밀번호가 틀렸습니다.')
    #         return redirect('signin')

    form = SigninForm()
    return render(request, 'sign_in.html', {'form': form})


def logout(request):
    auth.logout(request)
    return redirect(user_views.sign_in)
