from django.shortcuts import render,HttpResponse

# Create your views here.
def profile(request):
    return render(request,'account/profile.html')

def edit(request):
    return render(request,'account/edit-profile.html')