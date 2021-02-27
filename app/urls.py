from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('ecrites', views.predications_lists, name="predications")
]