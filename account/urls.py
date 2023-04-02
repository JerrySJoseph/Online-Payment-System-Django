from django.urls import path
from . import views

urlpatterns=[
  path('',views.profile,name='account'),
  path('profile/',views.profile,name='profile'),
  path('edit-profile/',views.edit,name='edit_profile')
]

