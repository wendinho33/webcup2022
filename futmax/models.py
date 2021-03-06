from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from embed_video.fields import EmbedVideoField


class FutUpload(models.Model):
    plans_choices = [
        ('BASIC', 'BASIC'),
        ('INTERMEDIATE', 'INTERMEDIATE'),
        ('STARTUP', 'STARTUP'),
        ('SUPREME', 'SUPREME'),
    ]
    payment_method = [
        ('Monthly', 'Monthly'),
        ('Yearly', 'Yearly'),
    ]

    pay_will = [
        ('Cash', 'Cash'),
        ('Credit Card', 'Credit Card'),
        ('Bitcoin', 'Bitcoin'),
        ('Ethereum', 'Ethereum'),
        ('FutCrypt', 'FutCrypt'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    images = models.ImageField(upload_to='futimages/')
    price = models.CharField(max_length=12, choices=plans_choices, default='BASIC')
    payment = models.CharField(max_length=7, choices=payment_method, default='MONTHLY')
    method = models.CharField(max_length=11, choices=pay_will, default='Cash')
    video = EmbedVideoField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while FutUpload.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField(max_length=255)

    def __str__(self):
        return self.name
