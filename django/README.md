## Django
# 虚拟环境
pip install virtualenv（virtualenv venv -p python3） 
python3 -m venv tutorial-env  
venv\scripts\activate（source venv/bin/activate）   
退出 虚拟环境 deactivate   

vscode虚拟环境： https://zhuanlan.zhihu.com/p/264796406  
rm -r shuak  删除

## linux
sudo apt install python3-venv  
python3 -m venv my-project-env  
source my-project-env/bin/activate  
pip install ...
如果导入成功，则安装了： python -c"import requests"  
deactivate  


### 创建django项目： 
django-admin startproject myproject  
cd myproject  
django-admin startapp 应用程序  
python manage.py runserver  


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
from django.urls import path,include
from django.contrib import admin
from demoapp import views

urlpatterns = [
    path('', include('demoapp.urls')),
    path('admin/', admin.site.urls),
]
settings.py
```

## 在app里加urls.py，连接include到项目的上一个urls.py
```
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
]
```
函数 path() 具有四个参数，两个必须参数：route 和 view  

django.contrib.admin — 管理员站点， 你很快就会使用它。
django.contrib.auth — 认证授权系统。
django.contrib.contenttypes — 内容类型框架。
django.contrib.sessions — 会话框架。
django.contrib.messages — 消息框架。
django.contrib.staticfiles — 管理静态文件的框架。  

## models.py
