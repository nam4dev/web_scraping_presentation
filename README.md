## Presentation of Web-Scraping techniques (Pymug)


This presentation intends to demonstrate the simplicity of web-scraping data 

to structure them in a Django Application.

It scrapes the Scrapy github pull requests data from https://github.com/scrapy/pulls

Taking advantage of Django Admin and some simple views to represent & visualize the data.

### Getting Started

Just clone the repository by typing in:

```bash
git clone https://github.com/nam4dev/web_scraping_presentation.git
```

[Create a python virtualenv](https://virtualenv.pypa.io/en/stable/installation/) in which you will install the requirements,

```bash
cd ./web_scraping_presentation
pip install requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open the web browser to http://127.0.0.1:8000/admin 

then login using credentials defined by the above command line (`createsuperuser`)

Then trigger the `github spider`,

```bash
scrapy runspider web_crawlers/spiders/github.py
```

Go to Authors and Pull Requests sections in the Django admin zone to visualize scrapped data.

Go on the root page http://127.0.0.1:8000 as well to visualize the data through custom views.