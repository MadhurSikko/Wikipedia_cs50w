from django.shortcuts import render
from django.urls import reverse
from django import forms
import markdown2
from . import util
from django.http import HttpResponseRedirect
import random

class newPageForm(forms.Form):
    title =  forms.CharField()
    body = forms.CharField(widget=forms.Textarea)

def markdownToHTML(name):
    content = markdown2.markdown(util.get_entry(name))
    return content

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def page(request, name):
    if name not in util.list_entries():
        return render(request, "encyclopedia/error.html", {
            "entry": False,
        })
    else:
        content = markdownToHTML(name)
        return render(request, "encyclopedia/page.html", {
            "content": content,
            "title": name,
        })
    
def newPage(request):
    if request.method == "POST":
        form = newPageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            body = form.cleaned_data["body"]
            
            if title not in util.list_entries():
                util.save_entry(title, body)
                return HttpResponseRedirect("wiki/"+title)
            else:
                return render(request, "encyclopedia/newPage.html", {
                    "form": newPageForm(),
                    "Error": True,
                })
            
    return render(request, "encyclopedia/newPage.html", {
        "form": newPageForm(),
    })

def randomPage(request):
    list = random.choice(util.list_entries())
    return HttpResponseRedirect("wiki/"+list)