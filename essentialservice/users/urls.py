from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('userdashboard/',views.userdashboard, name='userdashboard'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('search_service/', views.search_service, name='search_service'),
    path('electrical/', views.electrical, name='electrical'),
    path('plumbing/', views.plumbing, name='plumbing'),
    path('cleaning', views.cleaning, name='cleaning'),
    path('dailychores/', views.dailychores, name='dailychores'),
    path('records', views.records, name='records'),
]
