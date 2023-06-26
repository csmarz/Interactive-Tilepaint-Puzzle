# Render Page

import socket 
from django.http import HttpResponse
from django.template import loader

def Home(request):
    # hostname = socket.gethostname()
    # ip = socket.gethostbyname(hostname)
    # print(ip)
    # print(hostname)
    template = loader.get_template("a.html")
    return HttpResponse(
        template.render()
    )
