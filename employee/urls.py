from django.urls import path
from .views import emplist,empupdate,insert
urlpatterns = [
    path('emplist/',emplist.as_view()),
    path('empupdate/<int:pk>',empupdate.as_view()),
    path('insertemp/',insert.as_view() )
]
