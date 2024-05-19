from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.home, name="homepage"),
    # 傳給views.py的post_single函式，argument參數帶post，該型態為slug
    path('<slug:post>/', views.post_single, name='post_single'),
]