from django.shortcuts import render
from .utils.data import get_no_of_transactions,get_no_of_users,get_all_transactions,get_all_users
from .utils.view_utils import redirect_if_not_super_user
from .decorators import admin_required

@admin_required(login_url='login')
def index(request):
    context={
        'users':get_no_of_users(),
        'success_transactions':get_no_of_transactions(True),
        'pending_transactions':get_no_of_transactions(False)
    }
    return render(request,'administrator/dashboard.html',context)

@admin_required(login_url='login')
def all_users(request):
    redirect_if_not_super_user(request)
    context={
        'users':get_all_users(),        
    }
    return render(request,'administrator/all-users.html',context)


@admin_required(login_url='login')
def all_transactions(request):
    redirect_if_not_super_user(request)
    context={
        'transactions':get_all_transactions(),        
    }
    return render(request,'administrator/all-transactions.html',context)