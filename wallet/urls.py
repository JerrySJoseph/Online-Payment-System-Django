from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='wallet')
]

htmxpatterns=[
    path('/htmx/add-money',views.get_add_money,name='add-money')
]

urlpatterns+=htmxpatterns