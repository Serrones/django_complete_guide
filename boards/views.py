from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    print('request: ', request)
    print('request type: ', type(request))
    print('request dir: ', dir(request))
    print('request scheme: ', request.scheme)
    print('request method: ', request.method)
    print('request session: ', request.session)
    return HttpResponse('Hey World!!')
