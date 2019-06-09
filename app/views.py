from django.shortcuts import render

from app.models import Author
from app.models import PullRequest


def home(request):
    """
    Home view (root url)
    Basically a static view referencing both below dynamic views

    Args:
        request (django.http.HttpRequest): The request instance

    Returns:
        django.http.HttpResponse: The response instance
    """
    return render(request, 'index.html', {})


def visualize_pull_requests(request):
    """
    Pull requests view (/pulls)
    Display all Pull Request instance(s)

    Args:
        request (django.http.HttpRequest): The request instance

    Returns:
        django.http.HttpResponse: The response instance
    """
    pull_requests = PullRequest.objects.all().order_by('pid')
    return render(request, 'pull_requests.html', {'pull_requests': pull_requests})


def visualize_pull_requests_by_author(request):
    """
    Pull requests by Author view (/pulls/by/author)
    Display all Author instance(s) and related PR

    Args:
        request (django.http.HttpRequest): The request instance

    Returns:
        django.http.HttpResponse: The response instance
    """
    authors = Author.objects.all().order_by('name')
    return render(request, 'pull_requests_by_author.html', {'authors': authors})
