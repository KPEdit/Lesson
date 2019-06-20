from django.shortcuts import render, redirect
from django.conf import settings
from django.urls import reverse
from . import forms, models

# Create your views here.

def index(request):
    les = models.Lesson.objects.all()
    cat = models.Category.objects.all()
    return render(request, "main/index.html", context={'lessons':les,
                                                       'categories':cat})

def make_lesson(request):
    if request.method == 'POST':
        les = forms.LessonForm(request.POST)
        if les.is_valid():
            post = les.save(commit=False)
            if post.link == None:
                post.link = generate_link(post.title)
            post.author = request.user
            post.save()
            return redirect("/")

    form = forms.LessonForm()
    return render(request, 'main/make_lesson.html', {'form':form})

def generate_link(title):
    k = title.split(" ")
    t = "_".join(k)
    s = "{}".format(t)
    return s