# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from app.models import Author
from app.models import PullRequest


class GitHubPipeline(object):

    def process_item(self, item, spider):
        """
        Process a PullRequestItem
        Save the item into (django) database using ORM

        Args:
            item (web_crawlers.items.PullRequestItem): The item instance
            spider (web_crawlers.spiders.github.GitHubSpider): The Spider instance

        Returns:
            web_crawlers.items.PullRequestItem: The item instance
        """
        author, _ = Author.objects.get_or_create(**item['author'])

        pr, created = PullRequest.objects.get_or_create(pid=item['pid'])

        # May change over time, updating it
        pr.status = item["status"]

        if created:
            # Only on creation as those values shall not change over time
            pr.author = author
            pr.link = item["link"]
            pr.title = item["title"]
            pr.scrapped_uri = item["scrapped_uri"]

        pr.save()

        return item
