from django.http import HttpResponse,HttpResponseRedirect

from django.template import loader
from django.shortcuts import render
class Dog:
    def __init__(self):
        self.name = 'jinjin'
        self.age = 2
    def __str__(self):
        return f"this is a {self.age} dog,its name is {self.name}"
# path('',views.index_html)
def index_html(request):
    username = "ahuan"
    age = 14
    citys = ['beijing','shanghai','shenzhen','chengdu']
    person = {"pid":"1001","pname":"qtx"}
    def myfn():
        return "this is myfn function's value"
    mypet = Dog()
    # 方法1：
    # r = loader.get_template('index.html')
    # html = r.render()
    # return HttpResponse(html)
    # 方法2：使用locals()收集所有的局部变量，将变量名作为键，变量的值作为键拼接成字典；
    return render(request,'index.html',locals())

# path('mycal/',views.mycal_view)
def mycal_view(request):
    if request.method == 'GET':
        return render(request,'calc.html')
    elif request.method == 'POST':
        # 获取form表单提交的数据
        try:
            x = int(request.POST.get('x'))
            y = int(request.POST.get('y'))
        except:
            return HttpResponse("请输入整数")
        op = request.POST.get('op')
        if op == 'add':
            result = x + y 
        elif op == 'sub':
            result = x - y
        elif op == 'mul':
            result = x * y
        else:
            result = x / y
        return render(request,'calc.html',locals())

# path('free/',views.free_view)    http://127.0.0.1:8000/free/
def free_view(request):
    return render(request,'free.html')

# path('advanced/',views.advanced_view) http://127.0.0.1:8000/advanced/
def advanced_view(request):
    return render(request,'advanced.html')

# path('advanced/',views.live_view) http://127.0.0.1:8000/live/
def live_view(request):
    return render(request,'live.html')

# path('login/',views.login_view) http://127.0.0.1:8000/login/
from django.urls import reverse
def login_view(request):
    print('登录成功')
    # 根据别名解析出首页路由然后重定向到首页
    url = reverse('index')
    print(url)
    return HttpResponseRedirect(url)