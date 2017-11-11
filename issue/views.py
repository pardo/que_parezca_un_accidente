from django.shortcuts import render
from django.utils.deprecation import MiddlewareMixin
from rest_framework.authentication import BaseAuthentication
from django.contrib.auth.models import User
from rest_framework import exceptions



def home(request):
    return render(request, "base.html", {})

def add_issue(request):
    return render(request, "issue/add_issue.html", {
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
