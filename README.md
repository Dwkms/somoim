# Somoim - 커뮤니티 모임 관리 플랫폼

## 📌 프로젝트 소개

Somoim은 사용자들이 쉽고 편리하게 모임을 생성하고 관리할 수 있는 Django 기반 웹 애플리케이션입니다.

## 🛠 기술 스택

- **백엔드**: Django 5.2.3
- **데이터베이스**: SQLite
- **개발 언어**: Python
- **프론트엔드**: HTML, CSS, JavaScript

## ✨ 주요 기능

1. **사용자 관리**
   - 회원가입 및 인증 시스템
   - 프로필 관리

2. **모임 기능**
   - 모임 생성 및 참여
   - 모임 정보 공유
   - 위치 정보 제공

3. **커뮤니케이션**
   - 공지사항 게시판
   - 고객센터 지원

## 🚀 개발 과정 및 문제 해결

### 공지사항 페이지 디자인 개선

#### 문제 정의
- **초기 상황**: 공지사항 페이지의 디자인이 요구사항과 일치하지 않음
- **목표**: 미니멀하고 깔끔한 공지사항 페이지 구현

#### 해결 과정

1. **링크 연결 최적화**
   - `index.html`의 모든 공지사항 링크를 `{% url 'board:list' %}`로 수정
   - 정확한 라우팅 구현

2. **HTML 구조 개선**
   - 불필요한 Swiper 슬라이더 제거
   - 간결한 `<ul>`, `<li>` 태그 구조로 변경
   - 헤더와 푸터 제거로 미니멀한 디자인 추구

3. **CSS 모듈화**
   - `somoim_project/static/css/board.css` 파일 생성
   - 인라인 스타일 제거 및 외부 CSS 파일로 분리
   - 중앙 정렬 및 흰색 배경의 컨테이너 디자인 구현

#### 주요 학습 포인트
- 정확한 요구사항 이해의 중요성
- HTML 구조와 콘텐츠 렌더링 원칙
- CSS 파일 모듈화의 중요성
- 브라우저 개발자 도구를 활용한 디버깅

### 사용자 인증 시스템 개선

#### 문제 정의
- 기본 Django 인증 시스템의 한계
- 보안 및 사용자 경험 개선 필요

#### 해결 과정
- Django 기본 인증 시스템 확장
- 비밀번호 검증 로직 강화
- 사용자 프로필 모델 커스터마이징

## 🔧 개발 환경 설정

```bash
# 저장소 클론
git clone https://github.com/Dwkms/somoim.git
cd somoim

# 가상환경 생성 및 활성화
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# 의존성 설치
pip install -r requirements.txt

# 데이터베이스 마이그레이션
python manage.py migrate

# 개발 서버 실행
python manage.py runserver
```

## 📂 프로젝트 구조

```
somoim/
│
├── somoim_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── users/
├── board/
├── somoim/
├── customer/
└── accounts/
```

## 🔍 향후 개선 계획

- [ ] 소셜 로그인 통합
- [ ] 실시간 알림 시스템 구현
- [ ] 모바일 반응형 디자인 최적화
- [ ] 모임 검색 및 필터링 기능 강화

## 📜 라이선스

[적절한 오픈소스 라이선스 명시]

---

**더 자세한 정보는 [프로젝트 GitHub 저장소](https://github.com/Dwkms/somoim)를 참고해주세요.**
