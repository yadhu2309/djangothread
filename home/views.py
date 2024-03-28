from django.shortcuts import render

from .thread import *
# Create your views here.

def home(request):
    CreateStudentThread(5000).start()
    context={
        'data':'proccess started'
    }
    return render(request, 'index.html', context)