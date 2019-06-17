from django.contrib import admin
from . import models
# Register your models here.

class LessonAdmin(admin.ModelAdmin):
    exclude = ('date',)

class CategManagerAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Lesson,LessonAdmin)
admin.site.register(models.CategManager, CategManagerAdmin)