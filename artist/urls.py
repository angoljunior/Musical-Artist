from django.urls import path 
from . views import home ,listen ,categories ,search

urlpatterns = [
    path('', home ,name='home'),
    path('listen/<int:pk>/', listen ,name='listen'),
    path('category/<str:cat>/', categories ,name='category'),
    path('search/', search ,name='search')
]
