from django.http import HttpResponse

from django.template import loader
def index_html(request):
    r = loader.get_template('index.html')
    html = r.render()
    return HttpResponse(html)
