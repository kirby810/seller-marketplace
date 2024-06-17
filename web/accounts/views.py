# 지현 (로그인, 회원가입)
from allauth.account.views import SignupView, LoginView
from django.urls import reverse_lazy
# 지현 (마이페이지)
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# 재웅 (프로필 사진 수정)
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import EditProfileForm

# 지현 (마이페이지)
@login_required
def mypage_nav(request):
    return render(request, 'accounts/mypage_nav.html')

# @login_required
# def mypage_section(request, section):
#     return render(request, 'accounts/mypage_section.html', {'section': section})

@login_required
def mypage_section(request, section):
    if section == 'info':
        return render(request, 'accounts/edit_profile.html')
    else:
        return render(request, 'accounts/mypage_section.html', {'section': section})


# 지현 (로그인)
class CustomLoginView(LoginView):
    template_name = "accounts/login.html"  

# 지현 (회원가입)
class CustomSignupView(SignupView):
    template_name = 'accounts/signup.html'

# 재웅 (프로필 사진 수정)
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, '프로필이 성공적으로 업데이트되었습니다.')
            return redirect('profile')  # 프로필 페이지로 리디렉션
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'accounts/edit_profile.html', {'form': form})