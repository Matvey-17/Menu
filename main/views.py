from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def cars(request):
    return render(request, 'main/cars.html')
