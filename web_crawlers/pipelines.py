# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from app.models import Author
from app.models import PullRequest


class GitHubPipeline(object):
    """
    Class called on Spider creation & closure
    As well as on each processed item
    """

    @classmethod
    def from_crawler(cls, crawler):
        """
        Class method which instantiate the pipeline

        Args:
            crawler (scrapy.crawler.Crawler): The crawler instance

        Returns:
            GitHubPipeline: The pipeline instance
        """
        return cls(crawler)

    @classmethod
    def _clear_previous_data(cls):
        """
        Clear the previous rows from database
        to reflect perfectly the data over time

        Note:
            It is done in pretty brutal manner.
            A finer approach might thought of to finely determinate
            which rows are no longer existing and which one(s) shall be added
        """
        Author.objects.all().delete()
        PullRequest.objects.all().delete()

    def __init__(self, crawler):
        """
        Constructor

        Args:
            crawler (scrapy.crawler.Crawler): The crawler instance
        """
        self._crawler = crawler
        self._pull_requests = {}
        self._clear_previous_data()

    def close_spider(self, _):
        """
        Final processing
        Save all collected item(s) into (django) database using ORM

        Args:
            _ (web_crawlers.spiders.github.GitHubSpider): The Spider instance
        """
        for pr_id, pr_item in self._pull_requests.items():
            author, _ = Author.objects.get_or_create(**pr_item['author'])

            pr, created = PullRequest.objects.get_or_create(pid=pr_id)

            # May change over time, updating it
            pr.status = pr_item["status"]

            if created:
                # Only on creation as those values shall not change over time
                pr.author = author
                pr.link = pr_item["link"]
                pr.title = pr_item["title"]
                pr.scrapped_uri = pr_item["scrapped_uri"]

            pr.save()

    def process_item(self, item, _):
        """
        Process a PullRequestItem by storing it into a hash map

        Args:
            item (web_crawlers.items.PullRequestItem): The item instance
            _ (web_crawlers.spiders.github.GitHubSpider): The Spider instance

        Returns:
            web_crawlers.items.PullRequestItem: The item instance
        """
        self._pull_requests[item['pid']] = item
        return item
