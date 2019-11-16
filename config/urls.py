from django.contrib import admin
from django.urls import path, include
import dappajyeo.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dappajyeo.urls')),
    path('accounts/', include('accounts.urls')),
]
