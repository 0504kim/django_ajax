from urllib import request
from django.shortcuts import render

# posts
def todos(request): # request객체는 HTTP요청의 모든 것(재료와 호출명)을 담고 있음
    return render(request, 'todos.html') # 확장자까지 붙이는 걸 권장하고 있음