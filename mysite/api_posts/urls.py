from django.urls import path
from . import views

app_name = 'api_posts'

urlpatterns = [
    path('', views.get_posts, name='list'),
    path('<int:post_id>/', views.get_post, name='detail'),
    path('create/', views.create_post, name='create'),
    path('update/<int:post_id>/', views.update_post, name='update'),
    path('delete/<int:post_id>/', views.delete_post, name='delete'),
]