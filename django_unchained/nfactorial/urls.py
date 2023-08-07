from django.urls import path
from . import views

urlpatterns = [
    path('', views.print_hello, name='hello_nfactorial_school'),
    path('<int:first>/add/<int:second>/', views.sum_numbers, name='sum_of_numbers'),
    path('transform/<str:text>/', views.upper_text, name='upper_text'),
    path('check/<str:word>/', views.check_palindrome, name='check_palindrome'),
    path('calc/<int:first>/<str:operation>/<int:second>/', views.calculator, name='calculator'),
]