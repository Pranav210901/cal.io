from django.urls import path
#importing views from the global scope of count
from . import views
urlpatterns = [
    path('', views.bmr_cal, name='bmr_cal'),
]
