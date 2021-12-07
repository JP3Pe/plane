from django.contrib import auth
from django.shortcuts import render, redirect

from . import views as user_views
from .forms import SigninForm


# def register(request):
#     if request.method == "POST":
#         # 중복 유저 존재 하는지 검사하는 if문
#         if User.objects.filter(username=request.POST['username']):
#             messages.error(request, '해당 유저명은 이미 사용 중 입니다.')
#             return redirect('register')
#
#         form = UserRegisterForm(request.POST)
#         # 폼 검증
#         if form.is_valid():
#             new_user = User.objects.create_user(
#                 **form.cleaned_data)
#             auth.login(request, new_user)
#             return redirect(bulletin_board_views.show_post)
#     else:
#         form = UserRegisterForm()
#         return render(request, 'register.html', {'form': form})


def signin(request):
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
    return render(request, 'signin.html', {'form': form})


def logout(request):
    auth.logout(request)
    return redirect(user_views.signin)
