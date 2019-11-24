from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path('id_overlap_check/', views.id_overlap_check , name='id_overlap_check'),
    path('signup/', views.signup, name='signup'),
    path('sucecce/', views.sucecce, name='sucecce'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]