from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.




# Create your views here.
def index(request):
    return render(request, "index.html")


def shop(request):
    return render(request, "shop.html")


def cv(request):
    return render(request, "cv.html")

