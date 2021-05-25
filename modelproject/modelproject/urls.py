from django.contrib import admin
from django.urls import path
from blog.views import * # blogs.views에서 선언한 모든 것을 가져옴

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('<str:id>',detail,name='detail'),
]


# db의 id값을 지정해줍니다. 여기서 str은 문자열 형태를 의미하고, id는 앞서 views.py에서 정한 매개변수의 이름(id)입니다.
# 이렇게 하면, DB의 id값에 따라 페이지가 다르게 보이기도 하고, 이 값이 views.py에
# 매개변수로 들어가기도 하게 됩니다.
# 접근할 수 있게 하는 name을 설정해 줬습니다.