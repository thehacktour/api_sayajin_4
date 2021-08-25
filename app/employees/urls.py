from django.urls import path

from . import views

urlpatterns = [

    path('all/',views.AllEmployee.as_view()),
    path('add/',views.AddEmployee.as_view()),

]