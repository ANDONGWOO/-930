from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "day6/index.html")


def create(request):
    return render(request, "day6/create.html")
