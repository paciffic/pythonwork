from django.template import Template, Context
from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    t =  Template("<html><head><title>django test page</title></head><body><body><h1>It is {{ current_date}}.</h1></body></html>")
    html = t.render(Context({'current_date':now}))              
    
    return HttpResponse(html)

    