from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='admin'),
    path('all-users/',views.all_users,name='all-users'),
    path('all-transactions/',views.all_transactions,name='all-transactions')
]

htmxpatterns=[
    
]

urlpatterns+=htmxpatterns