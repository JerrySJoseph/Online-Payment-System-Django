from django.urls import path
from . import views

urlpatterns=[
  path('',views.index,name='profile'),
  
]

htmxpatterns=[
    path('htmx/nav-account-details/',views.nav_account_details,name='nav-account-details'),
    path('htmx/get-profile-html/',views.get_profile_html,name='get-profile-html'),
    path('htmx/recent-transfer-list/',views.get_recent_transfers,name='recent-transfer-list')
]

urlpatterns+=htmxpatterns

