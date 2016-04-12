from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic


def index(request):
    context = {}
    return render(request, 'index.html', context)