from django.urls import path
from Portfolio import views

urlpatterns = [
    path('', views.homePage, name='homepage'),
]