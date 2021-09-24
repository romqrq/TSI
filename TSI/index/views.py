from django.shortcuts import render
from django.http import HttpResponse

def index_view(request):
    """View that displays the index page"""
    return render(request, 'index.html')
