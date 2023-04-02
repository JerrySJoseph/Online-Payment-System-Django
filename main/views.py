from django.shortcuts import redirect, render
from django.contrib.auth import logout as _logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def index(request):
    return render(request,'main/dashboard.html',{'title':'Dashboard'})


def logout(request):
    _logout(request)
    return redirect('login')
