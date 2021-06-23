from django.contrib import admin
from django.urls import path
from blog.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('<int:id>', detail, name='detail'),
    path('new/', new, name='new'),
    path('create/', create, name='create'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete')
]
