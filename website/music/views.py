from django.http.response import HttpResponse


def home(request):
    """Default path view."""
    return HttpResponse('<br><h2 align="center">Welcome to Django Music Website!</h2>')
