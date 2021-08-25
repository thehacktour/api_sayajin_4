from django.urls import path

from . import views

urlpatterns = [

    path('all/',views.AllEmployee.as_view()),

]