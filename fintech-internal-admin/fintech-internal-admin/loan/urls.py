from django.urls import path

from loan import views

app_name = 'loan'
urlpatterns = [
    path('accounts/verify/loan/', views.verify_loans, name='all-loan'),
    path('accounts/approval/loan/', views.approval_loans, name='approval'),
]
