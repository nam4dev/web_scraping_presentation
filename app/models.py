from django.db import models


class Author(models.Model):
    """
    Model class Defining an Author of a Pull Request
    """
    name = models.CharField(unique=True, max_length=512)
    page_link = models.CharField(max_length=512)

    def __str__(self):
        return self.name


class PullRequest(models.Model):
    """
    Model class Defining a Pull Request
    """
    IS_OPEN = 'is_opened'
    IS_CLOSED = 'is_closed'
    IS_UNKNOWN = 'is_unknown'
    STATUS_CHOICES = (
        (IS_OPEN, 'Open',),
        (IS_CLOSED, 'Closed',),
        (IS_UNKNOWN, 'Unknown',),
    )

    pid = models.IntegerField(unique=True)
    title = models.CharField(max_length=512)
    link = models.URLField(max_length=512)
    status = models.CharField(
        max_length=len(IS_UNKNOWN),
        choices=STATUS_CHOICES,
        default=IS_UNKNOWN
    )
    scrapped_uri = models.URLField(max_length=512)
    # Reference on app.Author table
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='pull_requests')

    def set_status(self, readable_value):
        """
        Setter which manages the status value from
        human-readable value

        Args:
            readable_value (str): The human readable value from the spider
        """
        status = str(readable_value).lower()
        if status == 'open':
            self.status = PullRequest.IS_OPEN
        elif status == 'closed':
            self.status = PullRequest.IS_CLOSED
        else:
            self.status = PullRequest.IS_UNKNOWN

    def __str__(self):
        return '[{}] {}'.format(self.author.name, self.title)
