# somoim_project/somoim/admin.py

from django.contrib import admin
# from .models import YourModel # 만약 다른 모델을 등록했다면 이 줄은 그대로 두거나 삭제하세요.

# Django의 Session 모델을 임포트합니다.
from django.contrib.sessions.models import Session

# Session 모델을 관리자 페이지에서 커스터마이징하기 위한 Admin 클래스입니다.
class SessionAdmin(admin.ModelAdmin):
    # 세션 데이터를 사람이 읽을 수 있는 형태로 디코딩하여 보여주는 메서드입니다.
    def _session_data(self, obj):
        return obj.get_decoded()

    # 관리자 목록 페이지에 표시할 필드들입니다.
    list_display = ['session_key', '_session_data', 'expire_date']

    # 이 필드는 관리자 페이지에서 수정할 수 없도록 읽기 전용으로 설정합니다.
    readonly_fields = ['_session_data']

    # 만약 특정 필드를 필터링하고 싶다면 추가할 수 있습니다. (현재는 필요 없음)
    # filter_horizontal = []

    # 만약 특정 필드를 관리자 페이지에서 아예 숨기고 싶다면 추가할 수 있습니다. (현재는 필요 없음)
    # exclude = []

# Django 관리자 사이트에 Session 모델과 우리가 정의한 SessionAdmin 클래스를 등록합니다.
admin.site.register(Session, SessionAdmin)

# 만약 이전에 다른 모델을 등록했다면 여기에 해당 코드를 추가하세요. (예시)
# from .models import Post
# admin.site.register(Post)