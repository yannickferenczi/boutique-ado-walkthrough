from django.shortcuts import render

def index(request):
    """This function render the landing page of our web application"""
    return render(request, 'home/index.html')
