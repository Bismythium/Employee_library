from django.urls import path
from . import views

app_name='employeelib'

urlpatterns=[
    path('employee/',views.EmployeeView.as_view(),name='employeecreate'),
    path('employee/<int:pk>',views.EmployeeUpdateView.as_view(),name='employeeupdate'),
    path('employee/display/<int:pk>', views.EmployeeDetailView.as_view(),name='employeedetails')
    
] 