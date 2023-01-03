from django.urls import path
from .views import studlist,studupdate



urlpatterns = [
    path('slist/',studlist.as_view()),
    path('supdate/<int:pk>',studupdate.as_view()),
    

     
]
