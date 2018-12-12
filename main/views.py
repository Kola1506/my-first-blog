from django.shortcuts import render

# Create your views here.


def main_func(request):
    return render(request , 'main/1010.html' )

def mission_func(request):
    return render(request, 'main/02.html')

def history_func(request):
    return render(request, 'main/03.html')

def galery_func(request):
    return render(request , 'main/04.html')

def news_func_one(request):
    return render(request , 'main/news_one.html')

def reg_func(request):
    return render(request , 'main/reg.html')