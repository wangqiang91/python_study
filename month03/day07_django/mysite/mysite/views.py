from django.http import HttpResponse

# 视图函数
# 1、第一个参数必须是request对象；
# 2、视图函数必须有返回值，返回值通常是HttpResponse格式的对象；
def index_view(request):
    return HttpResponse('<script>alert("this is my django project")</script>','text/plain;charset=utf8')

def page_view(request):
    return HttpResponse('这是编号为1的网页')

def page_number_view(request,page_num):
    return HttpResponse(f'这是编号为{page_num}的网页')
def operation(request,num1,action,num2):
    if action == "add":
        return HttpResponse(f"{num1+num2}")
    elif action == "sub":
        return HttpResponse(f"{num1-num2}")
    elif action == "mul":
        return HttpResponse(F"{num1 * num2}")
    else:
        return HttpResponse("操作有误！！")

def re_operaation(request,num1,action,num2):
    num1 = int(num1)
    num2 = int(num2)
    if action == "add":
        result = num1 + num2
    elif action == "sub":
        result = num1 - num2
    elif action == "mul":
        result = num1 * num2
    else:
        return HttpResponse("操作有误！！")
    return HttpResponse(result)

def get_birthday(request,y,m,d):
    if len(y) == 4:
        return HttpResponse(f"生日为：{y}年{m}月{d}日")
    else:
        return HttpResponse("输入异常")

def demo_view(request):
    if request.method == "GET":
        print(request.GET)
        username = request.GET.get('username','default')
        # 数据有多个值时，用getlist
        answer = request.GET.getlist('answer')
        print(answer)
        return HttpResponse(f"get request success,welcome{username}")
    elif request.method == "POST":
        username = request.POST.get('username')
        return HttpResponse(f"post request success,welcome {username}")

def birthday_get(request):
    year = request.GET.get('year')
    month = request.GET.get('month')
    day = request.GET.get('day')
    return HttpResponse(f"your birthday is {year}year{month}month{day}day")

from django.template import loader
def temp_view(request):
    t = loader.get_template('demo.html')
    html = t.render()
    return HttpResponse(html)
