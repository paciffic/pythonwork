from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = ""
    html = html + "<html><head><title>django test page</title></head>"
    html = html + "<body><body><h1>It is now %s.</h1></body></html>" % now
    return HttpResponse(html)

    