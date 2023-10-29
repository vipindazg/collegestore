from django.urls import path
from . import views

urlpatterns = [
    path('department/<str:department>/', views.department_wikipedia, name='department_wikipedia'),
    path('login/', views.login, name='login'),
    path('base/', views.base, name='base'),
    path('', views.home, name='home'),
    path('registration/', views.registration, name='registration'),
    path('newpage', views.newpage, name='newpage'),
    path('orderconfirmation/', views.orderconfirmation, name='orderconfirmation'),

]