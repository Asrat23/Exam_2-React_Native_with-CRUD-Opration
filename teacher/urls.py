from django.urls import path
from .views import teachlist,teachupdate
urlpatterns = [
    path('teachlist/',teachlist.as_view()),
    path('teachupdate/<int:pk>',teachupdate.as_view()),
]
