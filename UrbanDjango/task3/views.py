from django.shortcuts import render

# Create your views here.

def home(request):
    title = 'Django'
    context = {
        'title': title,
    }
    return render(request, 'third_task/platform.html', context)

def moto(request):
    moto_catalog = ['Дорожные', 'Спортивные', 'Чоперы', 'Эндуро']
    title = 'Moto 365'
    context = {
        'moto_catalog': moto_catalog,
        'title': title,
    }
    return render(request, 'third_task/moto.html',context)

def basket(request):
    return render(request, 'third_task/basket.html')

