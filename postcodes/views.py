from django.http.response import HttpResponse
from django.shortcuts import render

from datetime import datetime

def index(request):
    d_now = datetime.now()
    Datetime = {
        'timestamp': d_now.strftime("%Y/%m/%d %H:%M:%S") ,
    }
    return render(request, 'index.html', Datetime)

