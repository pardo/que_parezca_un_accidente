from django.shortcuts import render


def home(request):
    return render(request, "base.html", {})

def add_issue(request):
    return render(request, "issue/add_issue.html", {
    })
