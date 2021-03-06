"""web_scraping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin

from app import views

urlpatterns = [
    path('', views.home),
    path('pulls/', views.visualize_pull_requests),
    path('pulls/by/author/', views.visualize_pull_requests_by_author),
    path('trigger/spider/github/', views.trigger_github_spider),
    path('add/project/to/scrapyd/', views.add_web_crawlers_project_to_scrapyd_server),
    path('admin/', admin.site.urls),
]
