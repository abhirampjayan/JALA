from django.urls import path
from . import views

urlpatterns = [
    path('',views.fakehome,name='fakehome'),
    path('result/',views.result,name='result')
]
