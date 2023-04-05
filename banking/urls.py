from django.urls import path
from . import views
from .apis import transfers as transfer_apis

urlpatterns = [
    path('send/', views.send, name='send-money'),
    path('request/', views.request, name='request-money'),
    path('transfer-request/', views.transfer_request, name='transfer-request'),
]

htmxpatters = [
    path('htmx/detail-form', views.detail_form, name='detail-form'),
    path('htmx/send-detail-form', views.send_detail_form, name='send-detail-form'),
    path('htmx/request-detail-form', views.request_detail_form,
         name='request-detail-form'),
    path('htmx/transfer-request-list',
         views.get_transfer_request_list, name='transfer-request-list'),
    path('htmx/withdraw-transfer-request-form',
         views.withdraw_confirmation_form, name='withdraw-form'),
    path('htmx/withdraw-transfer-request',
         views.withdraw_request, name='withdraw-request')

]

urlpatterns += htmxpatters
