from django.shortcuts import render
import markdown2
from . import util

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
