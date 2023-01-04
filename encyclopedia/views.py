import random

from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
import markdown2

from django.urls import reverse

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def text(request, text_title):
    content = util.get_entry(text_title)
    if content is None:
        raise Http404("Dose not exist.")

    return render(request, "encyclopedia/text.html", {
        "text_title": text_title,
        "content": markdown2.markdown(content)
    })


def search(request):
    q = request.POST.get("q")
    return HttpResponseRedirect(reverse("text", args=(q,)))


def add(request):
    return render(request, "encyclopedia/add.html")


def create(request):
    title = request.POST.get("title")
    content = "#" + request.POST.get("title") + '\n' + request.POST.get("text_content")
    util.save_entry(title, content)
    return HttpResponseRedirect(reverse("text", args=(title,)))


def rand(request):
    lis = util.list_entries()
    target = random.choice(lis)
    content = util.get_entry(target)
    return render(request, "encyclopedia/text.html", {
        "text_title": target,
        "content": markdown2.markdown(content)
    })


def edit(request, text_title):
    content = util.get_entry(text_title)
    if content is None:
        raise Http404("Dose not exist.")
    return render(request, "encyclopedia/edit.html", {
        "text_title": text_title,
        "content": content
    })