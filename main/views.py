from django.shortcuts import render, redirect
from django.conf import settings
from django.urls import reverse
from . import forms, models

# Create your views here.

# переписать index на page
# index должен содержать главную инфу о сайте и оглавление
# в page должно быть все то, что я написал для индекса, кроме выведения ВСЕХ УРОКОВ

def navig(form={}):
    end = form.copy()
    les = models.Lesson.objects.all()
    cat = models.Category.objects.all()
    end.update({'lessons':les,
                 'categories':cat})
    return end

def index(request):
    nav = navig()
    return render(request, "main/index.html", context=nav)

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
    form = {'form':form}
    nav = navig(form)
    return render(request, 'main/make_lesson.html', nav)


def make_category(request):
    if request.method == "POST":
        post = forms.CategoryForm(request.POST)
        if post.is_valid():
            post.save()
            return redirect('/')
    form = forms.CategoryForm()
    form = {'form':form}
    nav = navig(form)
    return render(request, 'main/make_category.html', nav)

def lesson(request, link):
    cur_les = models.Lesson.objects.get(link=link)
    if cur_les:
        nav = navig({'cur_les':cur_les})
        return render(request, 'main/lesson.html', context=nav)
    return render(request, '404.html')

def generate_link(title):
    k = title.split(" ")
    t = "_".join(k)
    s = "{}".format(t)
    return s