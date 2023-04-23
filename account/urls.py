from django.urls import path
from . import views

urlpatterns=[
  path('',views.profile,name='account'),
  path('profile/',views.profile,name='profile'),
  path('edit-profile/',views.edit,name='edit_profile')
]

htmxpatterns=[
    path('htmx/nav-account-details/',views.nav_account_details,name='nav-account-details')
]

urlpatterns+=htmxpatterns

