from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('<int:id>', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('new_with_django_form/', views.new_with_django_form, name='new_with_django_form'),
    path('create_with_django_form/', views.create_with_django_form, name='create_with_django_form')
]