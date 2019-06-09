# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AuthorItem(scrapy.Item):
    """
    Class defining an Author Item
    Follow the database model defined in our Django Application
    """
    name = scrapy.Field()
    page_link = scrapy.Field()


class PullRequestItem(scrapy.Item):
    """
    Class defining a PullRequest Item
    Follow the database model defined in our Django Application
    """
    pid = scrapy.Field()
    link = scrapy.Field()
    title = scrapy.Field()
    status = scrapy.Field()
    author = scrapy.Field()
    scrapped_uri = scrapy.Field()
