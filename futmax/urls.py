from django.urls import path
from futmax.views import futindex

urlpatterns = [
    path('', futindex, name='home'),
]