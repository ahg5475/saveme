from django.urls import path
from . import views


app_name = 'Dappajyeo'
urlpatterns = [
    path('', views.home, name='home'),
    path('training/', views.training, name='training'),
    path('calculrator/', views.calculator, name='calculator'),
    path('notice/', views.notice, name='notice'),
]