from django.urls import path
from . import views

app_name='signlog'
urlpatterns=[
    path('login/',views.pagelogin, name='login'),
    path('signup/',views.pagesignup, name='signup'),
]