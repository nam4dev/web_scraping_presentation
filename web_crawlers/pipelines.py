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

    def close_spider(self, spider):
        """
        Final processing
        Save all collected item(s) into (django) database using ORM

        Args:
            spider (web_crawlers.spiders.github.GitHubSpider): The Spider instance
        """
        spider.logger.info('Filling database with scrapped items ({})...'.format(len(self._pull_requests)))
        for idx, (pr_id, pr_item) in enumerate(self._pull_requests.items()):
            author, _ = Author.objects.get_or_create(**pr_item['author'])

            try:
                pr = PullRequest.objects.get(pid=pr_id)
            except PullRequest.DoesNotExist:
                pr = PullRequest()
                pr.pid = pr_id
                # Only on creation as those values shall not change over time
                pr.author = author
                pr.link = pr_item["link"]
                pr.title = pr_item["title"]
                pr.scrapped_uri = pr_item["scrapped_uri"]

            # May change over time, updating it
            pr.set_status(pr_item["status"])
            # Saving the PR item
            pr.save()
            spider.logger.info('[{}] Saved PR {} into database...'.format(idx + 1, pr))

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
