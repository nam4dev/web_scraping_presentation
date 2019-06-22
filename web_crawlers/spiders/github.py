import scrapy

from web_crawlers.items import AuthorItem
from web_crawlers.items import PullRequestItem


class GitHubSpider(scrapy.Spider):
    """
    Github Spider Class

    To be called from command line by typing in,

        > scrapy runspider web_crawlers/spiders/github.py
    """
    name = 'github'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/scrapy/scrapy/pulls']

    def parse(self, response):
        """
        Main parser method
        Parses all PR block, extracting title, link & scrapped URI

        Args:
            response (scrapy.http.response.Response): The response instance

        Yields:
            (scrapy.http.response.Response|
             web_crawlers.items.PullRequestItem): The response or Item instance
        """
        for title in response.xpath('//*[@data-hovercard-type="pull_request"]'):
            data = {
                'link': title.css('a::attr(href)').get(),
                'title': title.css('a ::text').get(),
                'scrapped_uri': response.url
            }
            yield response.follow(data['link'], callback=self.parse_pr, meta={'data': data})

        for next_page in response.css('a.next_page'):
            yield response.follow(next_page, self.parse)

    def parse_pr(self, response):
        """
        Parse the Pull Request status & author
        Build the final PullRequestItem instance

        Args:
            response (scrapy.http.response.Response): The response instance

        Yields:
            web_crawlers.items.PullRequestItem: Item instance
        """
        data = response.meta['data']

        github = self.allowed_domains[0]

        pr = PullRequestItem()
        pr['pid'] = int(str(data['link']).split('/').pop())
        pr['link'] = 'https://{}{}'.format(github, data['link'])

        pr['title'] = data['title']
        pr['scrapped_uri'] = data['scrapped_uri']

        selectors = response.xpath('//*[@id="partial-discussion-header"]/div[2]/div[1]/span/text()')
        if selectors and len(selectors) > 1:
            pr['status'] = selectors[1].get().strip()

        author = AuthorItem()

        author['name'] = response.xpath('//*[@id="partial-discussion-header"]/div[2]/div[2]/a/text()').get()
        author['page_link'] = 'https://{}/{}'.format(github, author['name'])

        pr['author'] = dict(author)

        yield pr
