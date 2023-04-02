from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',include('main.urls')),    
    path('iam/',include('iam.urls')),
    path('account/',include('account.urls'),name='account'),
    path('banking/',include('banking.urls'),name='banking'),
    path('notification/',include('notification.urls'),name='notification'),
    path('wallet/',include('wallet.urls'),name='wallet'),
    path('transaction/',include('transaction.urls'),name='transaction'),
    path('admin/',admin.site.urls,name='admin'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)