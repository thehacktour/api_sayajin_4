from django.urls import path

from . import views

urlpattern = [

    path('all/',views.AllEmployee.as_view()),

]