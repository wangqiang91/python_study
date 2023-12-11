from django.http import HttpResponse

# 视图函数
# 1、第一个参数必须是request对象；
# 2、视图函数必须有返回值，返回值通常是HttpResponse格式的对象；
def index_view(request):
    return HttpResponse('the first django server')

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