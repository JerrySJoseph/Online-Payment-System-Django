from django.shortcuts import render,HttpResponse
from transaction.utils.transactions import get_distinct_transactions_by_id
# Create your views here.
def index(request):
    return render(request,'account/index.html')


def get_profile_html(request):
    return render(request,'account/partials/profile.html')

def nav_account_details(request):
    return render(request,'account/partials/nav-account-details.html',{
        'user':request.user
    })

def get_recent_transfers(request):
    context={
        'transfers':get_distinct_transactions_by_id(request.user.id)
    }
    return render(request,'account/partials/recent-transfer-list.html',context)