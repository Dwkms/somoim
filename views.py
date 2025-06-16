# somoim_project/somoim/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from board.models import Post  # board 앱의 Post 모델 import

def index(request):
    """메인 페이지 뷰 - 최신 공지사항을 가져와서 전광판에 표시"""
    # 최신 공지사항 4개를 가져옴 (전광판에 표시할 개수)
    recent_notices = Post.objects.all().order_by('-created_at')[:4]
    
    context = {
        'recent_notices': recent_notices,
    }
    return render(request, 'index.html', context)

def location(request):
    return render(request, 'location.html')

def login_view(request):
    if request.method == 'POST':
        print("POST 요청이 들어왔습니다.") # 추가
        print("요청 POST 데이터:", request.POST) # 추가
        print("폼 데이터 유효성 검사 시작...") # 추가

        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            print("폼 유효성 검사 성공!") # 추가
            user = form.get_user()
            login(request, user)
            # messages.success(request, f"{user.username}님, 환영합니다!")
            return redirect('somoim:index') # 이 부분은 'somoim:index'로 수정 확인
        else:
            print("폼 유효성 검사 실패!") # 추가
            print("폼 오류:", form.errors) # 추가 (매우 중요!)
            messages.error(request, "로그인 정보가 올바르지 않습니다.")
    else:
        print("GET 요청이 들어왔습니다.") # 추가
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    # messages.info(request, "로그아웃 되었습니다.")
    return redirect('somoim:index') # 로그아웃 후 이동할 페이지