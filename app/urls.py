from django.urls import path
from .import views

urlpatterns = [

    path('', views.accueil, name='accueil'),
    #---- langue
    path('<slug:lang>/', views.index, name='index'),
    #---- Contact
    path('<slug:lang>/contact', views.contact, name='contact'),


    #---- predication
    path('<slug:lang>/predications', views.predications_lists, name="predications"),
    path('<slug:lang>/audio', views.predications_lists, name="audio"),
    path('<slug:lang>/predication/<int:num_pred>', views.predications_detail, name="predication"),
    path('<slug:lang>/result', views.result, name="result"),

    
    #---- actualite
    
]