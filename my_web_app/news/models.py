from django.db import models

# Create your models here.
class News_post(models.Model):
    title = models.CharField('Название новости', max_length=200)
    short_description = models.CharField('Краткое описание', max_length=200)
    text = models.TextField('Новость')
    content = models.TextField()
    pub_date = models.DateTimeField('Дата публикации')
