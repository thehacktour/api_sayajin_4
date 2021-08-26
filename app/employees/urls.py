from django.urls import path

from . import views

urlpatterns = [

    path('all/',views.AllEmployee.as_view()),
    path('add/',views.AddEmployee.as_view()),
    path('one/<int:id>/',views.SpecificEmployee.as_view()),

]