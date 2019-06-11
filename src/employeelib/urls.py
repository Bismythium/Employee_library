from django.urls import path
from . import views

app_name='employeelib'
urlpatterns=[
    path('empdetails/',views.EmployeeView.as_view(),name='employeedetails'),
    path('empdetails/<int:pk>',views.EmployeeDisplayView.as_view(),name='employeedisplay'),
]