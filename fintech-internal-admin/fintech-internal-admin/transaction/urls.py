from django.urls import path

from transaction import views

app_name = 'transaction'
urlpatterns = [
    path('accounts/internal/all-transaction/', views.all_transaction, name='all-transaction'),
    path('accounts/internal/approval-transaction/<str:id>/', views.approval_transaction, name='approval-transaction'),
]
