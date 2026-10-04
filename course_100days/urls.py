from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('clock_in/', views.clock_in, name='clock_in'),
    path('clock_out/', views.clock_out, name='clock_out'),
]

