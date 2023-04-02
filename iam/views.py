from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth import login as _login, authenticate
from iam.forms import RegisterForm, LoginForm
from django.contrib.messages import info, error,get_messages


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
            return error(request, 'Invalid username or password')
    form = LoginForm()
    message_store=get_messages(request)
    context={'title': 'Create account', 'form': form,'messages':message_store}
    message_store.used=True
    return render(request, 'iam/login.html', context)

# Create your views here.
