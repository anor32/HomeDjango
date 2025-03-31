from logging import exception

from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout, user_logged_out

# Create your views here.

from users.forms import UserRegisterForm, UserLoginForm


def user_register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()

            print(form.cleaned_data['password'])
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return HttpResponseRedirect(reverse('dogs:index'))
    context = {
        'title': 'Создать аккаунт',
        'form': UserRegisterForm
    }

    return render(request, 'users/user_register.html', context = context)


def user_login_view(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(email=cd['email'], password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('dogs:index'))
                else:
                    return HttpResponse('Аккаунт Неактивен!')
            else:
                print("Неверное имя пользователя или пароль")

    context = {
        'title': "Вход в аккаунт",
        'form': UserLoginForm
    }
    return render(request, "users/users_login.html", context=context)


def user_profile_view(request):
    user_object = request.user
    if user_object.first_name:
        user_name = user_object.first_name
    else:
        user_name = 'Anonymous'

    context = {
        'title': f'Ваш Профиль {user_name} '

    }
    return render(request, 'users/user_profile_read_only.html', context)


# добавить миграцию

def user_logged_out_view(request):
    logout(request)
    return redirect('dogs:index')


from django.shortcuts import render

# Create your views here.
