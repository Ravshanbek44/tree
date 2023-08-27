from django.db import models


class News(models.Model):
    title = models.CharField(max_length=400)
    image = models.ImageField(upload_to='news/')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'


class ForUsers(models.Model):
    name = models.CharField(max_length=221)
    image = models.ImageField(upload_to='forusers/')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'For Users'
        verbose_name_plural = 'For Users'
