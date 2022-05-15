from django.urls import path
from futmax.views import futindex, pricing, FutCreateView, ThankView, FutListView, FutDetailView, ContactView

urlpatterns = [
    path('', futindex, name='home'),
    path('thank/', ThankView.as_view(), name='thank_you'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('pricing/', pricing, name='pricing'),
    path('create/', FutCreateView.as_view(), name='create'),
    path('catalog/', FutListView.as_view(), name='list'),
    path('catalog/<slug:slug>', FutDetailView.as_view(), name='detail'),
]
