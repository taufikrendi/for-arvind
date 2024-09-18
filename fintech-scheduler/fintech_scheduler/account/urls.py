from django.urls import path

from account import views

app_name = 'account'
urlpatterns = [
	path('activate/<uidb64>/<token>/', views.activate, name='activate'),
	path('reset/<uidb64>/<token>/', views.reset_pass, name='reset'),
]