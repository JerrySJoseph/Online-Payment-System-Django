from django.shortcuts import render,HttpResponse

# Create your views here.
def profile(request):
    return render(request,'account/profile.html')

def edit(request):
    return render(request,'account/edit-profile.html')

def nav_account_details(request):
    return render(request,'account/partials/nav-account-details.html',{
        'user':request.user
    })