from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('detail/<int:id>', views.detail, name='detail'),
    path('detail/<int:id>/comment', views.comment, name='comment'),
]