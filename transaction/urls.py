from django.urls import path
from . import views

urlpatterns=[
       path('',views.index,name='transaction')
]

htmxpatterns=[
    path('htmx/getlist',views.get_list,name='get-list')
]

urlpatterns+=htmxpatterns