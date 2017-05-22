from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'personal/home.html')

def contact(reuest):
    return render(request,'personal/basic.html', {'content':['Contact me under the below mapge','mayank@gmail.com']})
