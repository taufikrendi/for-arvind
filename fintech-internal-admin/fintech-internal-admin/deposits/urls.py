from django.urls import path

from deposits import views

app_name = 'deposits'
urlpatterns = [
    path('accounts/internal/product-deposit/', views.all_deposit_product, name='all-deposit-product'),
    path('accounts/internal/product-deposit/add/', views.add_deposit_product, name='add-deposit-product'),
    path('accounts/internal/product-deposit/<str:id>/edit/', views.edit_deposit_product, name='edit-deposit-product'),
]
