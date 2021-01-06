from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    #return HttpResponse("<h1>Hello, WebSockets!</h1>")
    return render(request, 'app/index.html', {})
