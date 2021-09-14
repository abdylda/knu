from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'women/index.html')

def about(request):
    return render(request, 'women/about.html')

def knu(request):
    return render(request, 'women/index.html')

def knu(request):
    return render(request, 'women/about.html')

def parol(request):
    return render(request, 'women/parol.html')