## Django
# 虚拟环境
virtualenv venv -p python3  
source venv/bin/activate
退出 虚拟环境 deactivate  
pip install django==2.8.3  

### 创建django项目： django-admin startproject myproject  

python manage.py runserver  
django-admin startapp boards应用程序  

#### setting 'INSTALLED_APPS' 注册app
'boards',  # 译者注：建议和作者一样空一行来区别内置app和自定义的app  

### views.py 视图  
```
from django.http import HttpResponse
def home(request):
    return HttpResponse('Hello, World!')
 
```

### urls.py 
```
from django.conf.urls import url
from django.contrib import admin
from boards import views
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^admin/', admin.site.urls),
]
```

