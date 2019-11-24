from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'lists_board'

urlpatterns = [
    url(r'^$', views.Lists_board.as_view(), name='lists_main'),
    url(r'board/', views.Lists_board.as_view(), name='lists_board'),
    url(r'insert/', views.check_post, name='lists_board_insert'),
    url(r'^(?P<pk>[0-9]+)/detail/$', views.Lists_board_detail.as_view(), name='lists_board_detail'),
    url(r'^(?P<pk>[0-9]+)/update/$', views.Lists_board_update.as_view(), name='lists_board_update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.Lists_board_delete.as_view(), name='lists_board_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)