# from django.urls import path, include
# from movie_service.views import *
# import movie_servce.views

from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout,name='logout'),
]