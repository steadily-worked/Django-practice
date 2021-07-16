from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('signup/', views.signup_view, name='signup_view'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout, name='logout')
]