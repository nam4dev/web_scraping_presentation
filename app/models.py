from django.db import models


class Author(models.Model):
    """
    Model class Defining an Author of a Pull Request
    It follows the data structure one can found on github.com
    """
    name = models.CharField(unique=True, max_length=512)
    page_link = models.CharField(max_length=512)

    def __str__(self):
        return self.name


class PullRequest(models.Model):
    """
    Model class Defining a Pull Request
    It follows the data structure one can found on github.com
    """
    pid = models.IntegerField(unique=True)
    title = models.CharField(max_length=512)
    link = models.URLField(max_length=512)
    status = models.CharField(max_length=1024)
    scrapped_uri = models.URLField(max_length=512)

    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name='pull_requests')

    def __str__(self):
        author = 'Anonymous'
        if self.author:
            author = self.author.name
        return '[{}] {}'.format(author, self.title)
