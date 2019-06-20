from django.db import models
from django.conf import settings

# Create your models here.

# to add an OrderClass

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255,
                            blank=True,
                            unique=True,
                            null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               blank=True)
    categ = models.ForeignKey(Category,
                              on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title