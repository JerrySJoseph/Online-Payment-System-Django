from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from .forms import RequestForm, SearchForm, SendDetailForm
from django.http import Http404
from django.contrib.auth.decorators import login_required
from .utils.transfers import balance_check,transfer_money_by_id
from crispy_forms.templatetags.crispy_forms_filters import as_crispy_field
from django.core.exceptions import ValidationError
from .utils.search import get_user_with_id
from django.urls import reverse_lazy
from wallet.utils.exceptions.TransactionException import TransferException


@login_required(login_url='login')
def send(request):

    form = SearchForm()
    results = []
    # after confirmation
    if request.method == 'GET':
        if 'identifier' in request.GET:
            form = SearchForm(request.GET)

        if form.is_valid():
            results = form.search()

        return render(request, 'banking/layout/send.html', {'form': form, 'search_results': results})
    else:
        raise Http404()


@login_required(login_url='login')
def send_detail_form(request):
    print(f'user:{request.user}')
    if request.method == 'POST' and not 'confirm' in request.POST:
        recipient = get_user_with_id(request.POST.get('recipient'))
        form = SendDetailForm(request.user.id, request.POST)
        if form.is_valid():
            context = {
                'form': form,
                'recipient': recipient,
                'sender':request.user,
                'amount':request.POST.get('amount'),
                'currency':request.POST.get('currency')
            }
            return render(request, 'banking/partials/send_confirm_form.html', context)
        context = {
            'form': form,
            'recipient': recipient
        }
        return render(request, 'banking/partials/send_detail_form.html', context)
    
    elif request.method == 'POST' and 'confirm' in request.POST:
        
        try:
            sender_id=request.POST.get('sender')
            recipient_id=request.POST.get('recipient')
            amount=request.POST.get('amount')
            currency=request.POST.get('currency')
            transfer_money_by_id(sender_id,recipient_id,int(amount),currency)
            context = {
                'form': SendDetailForm(request.user.id,request.POST),
                'recipient': get_user_with_id(recipient_id),
                'sender':request.user,
                'amount':amount,
                'currency':currency
            }
            return render(request,'banking/partials/send_success.html',context)
        except TransferException as te:
            context={
                'message':te.message
            }
            return render(request,'banking/partials/send_failed.html',context)
        except Exception:
            return HttpResponse('Transaction Failed: ')
    
    elif 'recipient' not in request.GET:
        raise Http404()
    recipient = get_user_with_id(request.GET.get('recipient'))
    context = {
        'form': SendDetailForm(request.user.id),
        'recipient': recipient
    }
    return render(request, 'banking/partials/send_detail_form.html', context)
