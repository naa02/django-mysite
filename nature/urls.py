from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'nature'

urlpatterns = [
	# 서울 자연 관광지 현황
	path('forest0/', views.forest0, name='forest0'),
	# 인천 자연 관광지 현황
	path('forest1/', views.forest1, name='forest1'),
	# 경기도 자연 관광지 현황
	path('forest2/', views.forest2, name='forest2'),
	# 강원도 자연 관광지 현황
	path('forest3/', views.forest3, name='forest3'),
	# 부산 자연 관광지 현황
	path('forest4/', views.forest4, name='forest4'),
	# 제주도 자연 관광지 현원
	path('forest5/', views.forest5, name='forest5'),
	
	# 관광지 리뷰
	# path('comment2/<int:comment2_id>/', views.comment2, name='comment2'),
	# path('abc/comment2/', views.comment2, name='comment2'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
