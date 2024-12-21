from django.shortcuts import render

# Create your views here.

# posts
def posts(requests): # request객체는 HTTP요청의 모든 것(재료와 호출명)을 담고 있음
    return render('posts')