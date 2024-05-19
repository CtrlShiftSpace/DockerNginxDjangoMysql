from django.contrib import admin

# 資料表
from .models import Post

class AuthorAdmin(admin.ModelAdmin):
    # 要顯示的欄位
    list_display = ('title', 'status', 'slug', 'author')

# 註冊(register)資料表到後台
admin.site.register(Post, AuthorAdmin)