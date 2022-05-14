from django.urls import path
from user.views import user_login, user_logout, signup

urlpatterns = [
    path('', user_login, name='login'),
    path('register/', signup, name='signup'),
    path('logout/', user_logout, name='logout'),
]