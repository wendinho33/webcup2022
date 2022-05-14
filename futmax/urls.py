from django.urls import path
from futmax.views import futindex, pricing, FutCreateView

urlpatterns = [
    path('', futindex, name='home'),
    path('create/', FutCreateView.as_view(), name='create'),
]