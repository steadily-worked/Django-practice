from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('<int:id>', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
]