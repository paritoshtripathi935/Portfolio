from django.urls import path
from Portfolio import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
]