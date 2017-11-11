from django.shortcuts import render
from django.utils.deprecation import MiddlewareMixin


def home(request):
    return render(request, "base.html", {})

def add_issue(request):
    return render(request, "issue/add_issue.html", {
    })


class DisableCSRF(MiddlewareMixin):
    # for testing
    def process_request(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)
