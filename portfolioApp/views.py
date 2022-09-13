from django.shortcuts import render
from .models import Project

# Create your views here.



def index(request):

    portfolio = Project.objects.all()
    return render(request, 'portfolioApp/index.html', {'portfolio': portfolio})


def about(request):
    return render(request, 'portfolioApp/about.html')