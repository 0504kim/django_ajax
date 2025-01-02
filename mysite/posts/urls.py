from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.posts, name='view'),
    # path('jquery', views.posts_jquery, name='jquery'),
]