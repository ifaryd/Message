from django.urls import path
from .import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('ecrites', views.predications_lists, name="predications")
=======
    path('', views.accueil, name='accueil'),
    path('<slug:lang>/', views.index, name='index'),
    path('<slug:lang>/contact', views.contact, name='contact'),
    path('<slug:lang>/predications', views.predications_lists, name="predications"),
    path('<slug:lang>/predication/<int:predid>', views.predications_detail, name="predication")
>>>>>>> 7df1736bec72cb050e8b54585f68ad3e72d8f4c5
]