from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name='Category title')
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    parent_id = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url_articles_by_category_id(self):
        return reverse('get_articles_by_category_id', kwargs={'category_id': self.id})


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='Article title')
    description = models.TextField(verbose_name='Article description')
    image = models.ImageField(verbose_name='Article image', upload_to='photos/%Y/%m/%d')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}: Created at - {self.created_at}, Updated at - {self.updated_at}'

    def get_absolute_url_articles_edit(self):
        return reverse('edit_article', kwargs={'article_id': self.id})

    def get_absolute_url_articles_delete(self):
        return reverse('delete_article', kwargs={'article_id': self.id})
