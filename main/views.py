from django.shortcuts import render, redirect
from django.conf import settings
from django.urls import reverse
from . import forms, models

# Create your views here.

# переписать index на page
# index должен содержать главную инфу о сайте и оглавление
# в page должно быть все то, что я написал для индекса, кроме выведения ВСЕХ УРОКОВ
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

def lesson(request, link):
    cur_les = models.Lesson.objects.get(link=link)
    if cur_les:
        les = models.Lesson.objects.all()
        cat = models.Category.objects.all()
        return render(request, 'main/lesson.html', context={'lessons':les,
                                                            'categories':cat,
                                                            'cur_les':cur_les})
    return render(request, '404.html')

def generate_link(title):
    k = title.split(" ")
    t = "_".join(k)
    s = "{}".format(t)
    return s