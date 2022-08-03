from django.db import models


class Scope(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя тега')
    
    class Meta:
        verbose_name = 'Сфера'
        verbose_name_plural = 'Сферы'

    def __str__(self):
        return self.name


class Article(models.Model): 

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    scope = models.ManyToManyField(Scope, related_name='articles', through='ArticleScope')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class ArticleScope(models.Model):

    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    tag = models.ForeignKey(Scope, on_delete=models.SET(None), related_name='scopes', verbose_name = 'Раздел')
    is_main = models.BooleanField(default=False, verbose_name='Главный')

    class Meta:
        verbose_name = 'Тематика статьи'
        verbose_name_plural = 'Темитики статей'
        ordering = ['-is_main']
