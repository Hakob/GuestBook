from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('sign/', views.SignView.as_view(), name='sign')
]
