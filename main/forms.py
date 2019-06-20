from . import models
from django import forms

class LessonForm(forms.ModelForm):

    class Meta:
        model = models.Lesson
        fields = '__all__'