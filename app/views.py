import requests
import scrapyd_api

from django.shortcuts import render

from app.models import Author
from app.models import PullRequest

scrapyd = scrapyd_api.ScrapydAPI()


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


def trigger_github_spider(request):
    """
    Trigger the github spider through scrapyd server
    It sends a POST request to the scrapyd REST API to schedule the job

    Args:
        request (django.http.HttpRequest): The request instance

    Returns:
        django.http.HttpResponse: The response instance
    """
    messages = []
    data = dict(project='web_crawlers', spider='github')
    try:
        # Just to demonstrate that scrapyd acts as a REST API
        # response = requests.post('http://localhost:6800/schedule.json', data=data)
        # uid = response.json()['jobid']

        # scrapyd_api
        uid = scrapyd.schedule(**data)
        messages.append(
            {
                'type': 'info',
                'text': '{project}.{spider} triggered with JOB ID: {uid}'.format(uid=uid, **data)
            }
        )
    except (requests.exceptions.ConnectionError,
            scrapyd_api.exceptions.ScrapydResponseError,
            KeyError, Exception) as e:
        messages.append(
            {
                'type': 'error',
                'text': '{project}.{spider} could not be triggered due to: {e}'.format(e=e, **data)
            }
        )

    return render(request, 'index.html', {'messages': messages})
