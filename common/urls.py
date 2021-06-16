from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'common'

urlpatterns = [
	path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
	path('signup/', views.signup, name='signup'),
	# 서울 자연 관광지 현황
	path('forest/', views.forest, name='forest'),
	# 경기도 자연 관광지 현황
	path('forest2/', views.forest2, name='forest2'),
	# 강원도 자연 관광지 현황
	path('forest4/', views.forest4, name='forest4'),
	# 제주도 자연 관광지 현원
	path('forest3/', views.forest3, name='forest3'),
	# 관광지 리뷰
	path('comment2/', views.comment2, name='comment2'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)