from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def Shilpa(request):
    return HttpResponse('Shilpa is cute and gorgeous')

def maheshnaik(request):
    return HttpResponse('maheshnaik is a play boy')