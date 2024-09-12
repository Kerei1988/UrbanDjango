from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render
from .forms import UserRegister


# Create your views here.


def sign_up_by_django(request):
    users = ['Nikita', 'Denis', 'Rinat']
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.Post)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        repeat_password = form.cleaned_data['repeat_password']
        age = form.cleaned_data['age']
        if password == repeat_password and age >= 18 and username not in users:
            return HttpResponse(f'Приветствуем, {username}!')
        if password != repeat_password:
            info['error'] = 'Пароли не совпадают!'
            return render(request, 'fifth_task/registration_page.html', {'info': info})
        if age < 18:
            info['error'] = 'Вы должны быть старше 18!'
            return render(request, 'fifth_task/registration_page.html', {'info': info})
        if username in users:
            info['érror'] = 'Такое имя уже существует'
            return render(request, 'fifth_task/registration_page.html')
    else:
        form = UserRegister()
    return render(request, 'fifth_task/registration_page.html', {'form': form})


def sign_up_by_html(request):
    users = ['Nikita', 'Denis', 'Rinat']
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        if password == repeat_password and int(age) >= 18 and username not in users:
            return HttpResponse(f'Приветствуем, {username}!')
        if password != repeat_password:
            info['error'] = 'Пароли не совпадают!'
            return render(request, 'fifth_task/registration_page.html', {'info': info})
        if int(age) < 18:
            info['error'] = 'Вы должны быть старше 18!'
            return render(request, 'fifth_task/registration_page.html', {'info': info})
        if username in users:
            info['error'] = 'Такое имя уже существует'
            return render(request, 'fifth_task/registration_page.html', {'info': info})
    return render(request, 'fifth_task/registration_page.html')
