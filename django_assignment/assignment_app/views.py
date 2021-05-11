from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
def index(request):
    data = {
        'Name': 'Jess Lam',
        'Track': 'Backend - Python',
        'Message': 'Hello instructor, thanks in advance for a great grade!'
    }
    print(data)
    return HttpResponse(json.dumps(data))
