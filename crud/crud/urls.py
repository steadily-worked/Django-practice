from django.contrib import admin
from django.urls import path, include
# include 작업을 분리해서, 앱의 urls.py로 넘겨준다.
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name='home'),
    path('blog/', include('blog.urls')),
]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', home, name='home'),
#     path('<str:id>', detail, name='detail'),
#     path('new/', new, name='new'),
#     path('create/', create, name='create'),
#     path('update/<int:id>', update, name='update'),
#     path('delete/<str:id>', delete, name='delete')
# ]
