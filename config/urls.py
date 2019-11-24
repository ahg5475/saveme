from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dappajyeo.urls')),
    path('accounts/', include('accounts.urls')),
    path('lists_board/', include('lists_board.urls')),
]
