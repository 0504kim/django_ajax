from django.urls import path
from . import views

app_name = 'api_posts'

urlpatterns = [
    path('api/posts/', views.get_posts, name='get_posts'),
    path('api/posts/<int:post_id>/', views.get_post, name='get_post'),
    path('api/posts/create/', views.create_post, name='create_post'),
    path('api/posts/update/<int:post_id>/', views.update_post, name='update_post'),
    path('api/posts/delete/<int:post_id>/', views.delete_post, name='delete_post'),
]