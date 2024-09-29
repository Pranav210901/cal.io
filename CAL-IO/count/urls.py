from django.urls import path
#importing views from the global scope of count
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('food_cal/', views.food_cal, name='food_cal'),
]
