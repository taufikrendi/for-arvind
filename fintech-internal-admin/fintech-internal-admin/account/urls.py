from django.urls import path
from django.contrib.auth import views as auth_views

from account import views

app_name = 'account'
urlpatterns = [
	path('', views.user_login, name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),

	path('accounts/internal/dashboard/', views.dashboard, name='dashboard'),
	path('accounts/internal/all-member/', views.all_member, name='all-member'),
	path('accounts/internal/approval-member/<str:id>/', views.approval_member, name='approval-member'),
]