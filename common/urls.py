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
	# 관광지 리뷰
	path('review/', views.review, name='review'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)