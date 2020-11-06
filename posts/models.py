from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    image = models.URLField(max_length=500)
    title = models.CharField(max_length=100)
    body = MarkdownxField()
    published_date = models.DateTimeField(blank=True, null=True)

    def formatted_markdown(self):
        return markdownify(self.body)

    def body_summary(self):
        return markdownify(self.body[:250] + "...")

class Comments(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    comment = models.TextField()
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    moderator = models.BooleanField(default=False)

    
