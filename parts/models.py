

from django.forms.models import fields_for_model
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('carparts:product_list_by_category',
                        args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products',on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    photo = models.ImageField(upload_to ='uploads/')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('carparts:product_detail',
                        args=[self.id, self.slug])



class Slider(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(upload_to ='uploads/')

    class Meta:
        ordering = ('name',)
        
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдеры'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile' 