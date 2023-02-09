from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views

# http://127.0.0.1/users
app_name='users'
urlpatterns = [
    path('signup/',views.signup,name='signup'), #form 보여줘
    path('signupProcess/',views.signup_process,name='signupProcess'),
    # 회원정보 DB저장해 
    
    path('login/',views.login,name='login'), #폼보여줘
    path('logout/',views.logout,name='logout'),  #로그아웃하고 세션삭제
    path('loginProcess/',views.login_process,name='loginProcess'),  #로그인여부 판단
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
   #js, css, image  정적 파일 관리 (Django가 webserver 역활을 함)