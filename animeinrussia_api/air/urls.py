from django.urls import path

from . import views

urlpatterns = [
    path('shows/', views.index, name='index'),
]
