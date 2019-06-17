from django.db import models

# Create your models here.

class ABS_Lesson(models.Model):
    title = None

    def __str__(self):
        return self.title

class Lesson(ABS_Lesson):
    title = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)
    content = models.TextField()
    #link = models.CharField(max_length=255)
    # author = models.One


class CategManager(ABS_Lesson):
    title = models.CharField(max_length=255)
    #sub_lessons = models.ManyToOneRel()