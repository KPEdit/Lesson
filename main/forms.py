from . import models
from django import forms
# from django.utils.translation import gettext_lazy as _


class LessonForm(forms.ModelForm):

    class Meta:
        model = models.Lesson
        fields = '__all__'
        # help_texts = {
        #     'link': _("Write down Your own link, if You want")
        # }


class CategoryForm(forms.ModelForm):

    class Meta:
        model = models.Category
        fields = '__all__'
