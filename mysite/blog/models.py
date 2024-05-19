from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):

    # 篩選條件
    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = {
        ('draft', 'Draft'),
        ('published', 'Published'),
    }

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish_date')
    publish_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    status = models.CharField(max_length=10, choices=options, default='draft')
    # 這段objects就是預設的Manager，只是一般忽略此段，所以在views.py中才會使用Post.objects.all()來取得所有Post
    objects = models.Manager() # default manager
    # 另外建立一個新的Manager，但此Manager和objects相比增加了get_queryset方法可以使用
    newmanager = NewManager() # custom manager

    class Meta:
        # 升冪 (由小到大)
        ordering = ('publish_date',)
        # 降冪 (由大到小)
        # ordering = ('-publish_date',)

    def __str__(self):
        return self.title

    # 路徑連結
    def get_absolute_url(self):
        # post_single是urls.py中定義的name
        return reverse('blog:post_single', args=[self.slug])
