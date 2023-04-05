from django.shortcuts import render,HttpResponse
from django.http import Http404
from .utils.transactions import get_transactions_by_id
from .filters import TransactionFilter

# Create your views here.
def index(request):
    if request.method=='GET':
        transactions=get_transactions_by_id(request.user.id)
        filter=TransactionFilter(request.GET,queryset=transactions)
        transactions=filter.qs
        context={
            'transactions':transactions,
            'filter':filter
        }
        return render(request,'transaction/layout/list.html',context)
    raise Http404()

def get_list(request):
    if request.method=='GET':
        transactions=get_transactions_by_id(request.user.id)
        filter=TransactionFilter(request.GET,queryset=transactions)
        transactions=filter.qs
        context={
            'transactions':transactions,
            'filter':filter
        }
        return render(request,'transaction/partials/transaction-table.html',context)
    raise Http404()