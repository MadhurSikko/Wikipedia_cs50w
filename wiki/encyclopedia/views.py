from django.shortcuts import render
from django.urls import reverse
from django import forms
import markdown2
from . import util
from django.http import HttpResponseRedirect
import random

class editPageForm(forms.Form):
    body = forms.CharField(widget=forms.Textarea)

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
        return HttpResponseRedirect(reverse("encyclopedia:error"))
    else:
        content = markdownToHTML(name)
        return render(request, "encyclopedia/page.html", {
            "content": content,
            "title": name,
        })
    
def error(request):
    return render(request, "encyclopedia/error.html")

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

def searchPage(request):
    if request.method == "POST":
        search = request.POST['q']
        if search in util.list_entries():
            return HttpResponseRedirect("wiki/"+search)
        else:
            for entry in util.list_entries():
                if search in entry:
                    return HttpResponseRedirect("wiki/"+entry)
    return HttpResponseRedirect(reverse("encyclopedia:error"))

def editPage(request, name):
    form = editPageForm(initial={'body': util.get_entry(name)})
    if request.method == "POST":
        form = editPageForm(request.POST)
        if form.is_valid():
            body = form.cleaned_data["body"]
            
            if name in util.list_entries():
                util.save_entry(name, body)
                return HttpResponseRedirect("/wiki/"+name)
    return render(request, "encyclopedia/editPage.html", {
        "form": form,
    })

