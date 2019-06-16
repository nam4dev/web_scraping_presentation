from setuptools import setup
from setuptools import find_packages

setup(
    name='web_crawlers',
    version='0.0.1',
    packages=find_packages(),
    url='',
    license='MIT',
    author='Namgyal BRISSON',
    author_email='n.brisson@apy-consulting.com',
    description=(
        'Simple demonstration of web-scraping techniques '
        'through scrapy for the Pymug presentation'
    ),
    entry_points={
        'scrapy': [
            'settings = web_crawlers.settings'
        ]
    },
)
