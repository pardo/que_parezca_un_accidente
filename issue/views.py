from django.shortcuts import render, redirect
from django.utils.deprecation import MiddlewareMixin
from rest_framework.authentication import BaseAuthentication
from django.contrib.auth.models import User
from rest_framework import exceptions



def home(request):
    if request.user.is_authenticated():
        return redirect(issue_list)
    return render(request, "base.html", {})

def add_issue(request):
    if not request.user.is_authenticated():
        return redirect(home)

    return render(request, "issue/add_issue.html", {
    })


def issue_view(request, issue_uuid):
    return render(request, "issue/view_issue.html", {
        "issue_url": "/issues/%s/" % issue_uuid
    })



def issue_list(request):
    if not request.user.is_authenticated():
        return redirect(home)

    return render(request, "issue/issue_list.html", {
    })


class DisableCSRF(MiddlewareMixin):
    # for testing
    def process_request(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)


class TokenBonita(BaseAuthentication):
    """
    HTTP Basic authentication against username/password.
    """
    www_authenticate_realm = 'api'

    def authenticate(self, request):
        if request.GET.get("token") == "bonita":
            return (User.objects.filter(is_staff=True).first(), None)
        elif "token" in request.GET:
            raise exceptions.AuthenticationFailed("Auth error")
