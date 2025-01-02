from django.db import models

# Create your models here.
class Post(models.Model): # model은 각각의 데이터 하나를 다루기 때문에 단수
    title = models.CharField(max_length=100)
    content = models.TextField()
    
    class Meta:
        db_table = 'posts'
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        
    def __str__(self):
        return self.title