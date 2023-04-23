from django.shortcuts import render
from banking.utils.bank_account import get_all_bank_accounts
from utils.toast import ToastHttpResponse
from .utils.wallet import add_money_to_wallet
from decimal import Decimal
from .forms import AddMoneyForm
from utils.views.empty import empty_view
# Create your views here.


def index(request):
    context = {
        'accounts': get_all_bank_accounts(request.user.id)
    }
    return render(request, 'wallet/layout/index.html', context)


def get_add_money(request):

    if request.method == 'POST':
        form = AddMoneyForm(request.POST)
        if form.is_valid():
            amount = request.POST.get('amount')
            add_money_to_wallet(request.user.wallet, Decimal(
                amount), request.user.wallet.currency)
            return ToastHttpResponse(True, 'Money Credited', f'{amount} added successfully to your wallet')
        else:
            context = {
                'form': form
            }
            return render(request, 'wallet/partials/add_money_amount_form.html', context)

    if 'id' in request.GET:
        context = {
            'form': AddMoneyForm()
        }
        return render(request, 'wallet/partials/add_money_amount_form.html', context)
    accounts=get_all_bank_accounts(request.user.id)
    
    if len(accounts)<=0:
        return empty_view(request,'No Banks added','You have not added any accounts yet.')
    context = {
        'accounts': accounts
    }
    return render(request, 'wallet/partials/add_money_bank_select.html', context)
