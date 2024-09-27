from django.urls import path
from .views import EmployeeCreateView

app_name='employee'

urlpatterns=[
    path('', EmployeeCreateView.as_view(),name='employee'),
]