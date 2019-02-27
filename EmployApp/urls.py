from django.urls import path
from . import views


urlpatterns = [
    # route for the index function and home.html
    path('', views.index, name='index'),
    # route for the employAppResults.html
    path('employAppResults/', views.index, name='employAppResults')
]