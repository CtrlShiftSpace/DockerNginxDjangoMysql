from django.shortcuts import render, get_object_or_404
from .models import Post

def home(request):

    # 將原先 all_posts = Post.objects.all() 修改為以下
    all_posts = Post.newmanager.get_queryset()
    return render(request, 'index.html', {'posts': all_posts})

def post_single(request, post):

    # 嘗試取得slug欄位等於post參數值的資料，如果找不到就回傳404
    post = get_object_or_404(Post, slug=post, status='published')
    return render(request, 'single.html', {'post': post})