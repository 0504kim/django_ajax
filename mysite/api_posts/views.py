from urllib import request
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from posts.models import Post

# 목록
def get_posts(request):
    posts = Post.objects.all()
    posts_list = []
    for post in posts:
        posts_list.append({
            'id': post.id,
            'title': post.title,
            'content': post.content,
        })
    return JsonResponse(posts_list, safe=False)

# 상세
def get_post(request, post_id):
    posts = get_object_or_404(Post, id=post_id)
    return JsonResponse(posts, safe=False)

# 생성
def create_post(request):
    title = request.POST['title']
    content = request.POST['content']
    post = Post(title=title, content=content)
    post.save()
    return JsonResponse(post, safe=False)

# 수정
def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.title = request.POST['title']
    post.content = request.POST['content']
    post.save()
    return JsonResponse(post, safe=False)

# 삭제
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return JsonResponse({'result': 'success'}, safe=False)