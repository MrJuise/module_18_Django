from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister

# Create your views here.
users = ['Vasya', 'Petya', 'Anna']


def sign_up_by_django(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            return HttpResponse(f'Приветствуем {username}')
    else:
        form = UserRegister()
    return render(request, 'fifth_task/reg_form.html', {'form': form})


def sign_up_by_html(request):
    info = {}
    context = {
        'info': info,
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if password != repeat_password:
            info.update({'error': 'Пароли не совпадают'})
            return render(request, 'fifth_task/registration_page.html', context)

        try:
            age = int(age)
            if age < 18:
                info.update({'error': 'Вы должны быть старше 18'})
                return render(request, 'fifth_task/registration_page.html', context)
        except ValueError:
            info.update({'error': 'Введите корректный возраст'})
            return render(request, 'fifth_task/registration_page.html', context)

        if username in users:
            info.update({'error': f'Пользователь {username} уже существует'})
            return render(request, 'fifth_task/registration_page.html', context)

        return HttpResponse(f'Приветствуем, {username}')

    return render(request, 'fifth_task/registration_page.html', context)
