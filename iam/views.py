from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login as _login, authenticate
from iam.forms import RegisterForm, LoginForm
from django.contrib.messages import info, error, get_messages
from utils.toast import ToastHttpResponse


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'iam/register.html', {'title': 'Create account', 'form': form})
    else:
        return render(request, 'iam/register.html', {'title': 'Create account', 'form': RegisterForm()})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                _login(request, user)
                return HttpResponseRedirect('/')
            else:
                error(request, 'Invalid username or password')

        else:
            error(request, 'Invalid username or password')
            message_store = get_messages(request)
            context = {'title': 'Sign In',
               'form': form, 'messages': message_store}
            return render(request, 'iam/login.html', context)
    form = LoginForm()
    message_store = get_messages(request)
    context = {'title': 'Sign In',
               'form': form, 'messages': message_store}
    message_store.used = True
    return render(request, 'iam/login.html', context)



def get_register_form(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except Exception as e:
                return ToastHttpResponse(False, 'Error Occured', str(e))
    message_store = get_messages(request)
    context = {
        'form': form,
        'messages': message_store}
    message_store.used = True
    return render(request, 'iam/partials/register_form.html', context)


def get_login_form(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    _login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    error(request, 'Invalid username or password')
            except Exception as e:
                return ToastHttpResponse(False, 'Error Occured', str(e))
    message_store = get_messages(request)
    context = {
        'form': form,
        'messages': message_store}
    message_store.used = True
    return render(request, 'iam/partials/login_form.html', context)
