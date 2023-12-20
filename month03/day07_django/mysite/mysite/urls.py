"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/admin/
    path('admin/', admin.site.urls),
    # http://127.0.0.1:8000/
    path('',views.index_view),
    # http://127.0.0.1:8000/page/1/
    path('page/1/',views.page_view),
    # http://127.0.0.1:8000/page/xxx
    path('page/<int:page_num>/',views.page_number_view),
    # http://127.0.0.1:8000/num1/add_sub_mul/num2
    # path('<int:num1>/<str:action>/<int:num2>/',views.operation),
    #正则表达式匹配数据，地址同上
    re_path(r'^(?P<num1>\d{1,2})/(?P<action>\w+)/(?P<num2>\d{1,2})/$',views.re_operaation),
    # http://127.0.0.1:8000/birthday/4位数字/1-2位数字/1-2位数字
    re_path(r'birthday/(?P<y>\d{4})/(?P<m>\d{1,2})/(?P<d>\d{1,2})',views.get_birthday),
    re_path(r'birthday/(?P<m>\d{1,2})/(?P<d>\d{1,2})/(?P<y>\d{4})',views.get_birthday),

    path('demo/',views.demo_view),

    path('birthday/',views.birthday_get),

    path('temp/',views.temp_view)
]
