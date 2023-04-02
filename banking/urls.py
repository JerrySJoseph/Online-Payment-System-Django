from django.urls import path
from . import views
from .apis import transfers as transfer_apis

urlpatterns=[
  path('send/',views.send,name='send-money'),
]

htmxpatters=[
    path('htmx/send-amount-form',views.send_detail_form,name='send-detail-form')
]

urlpatterns+=htmxpatters