## [Pymug] Presentation of Web-Scraping techniques

This presentation intends to demonstrate the simplicity of web-scraping data 

to structure it in a Django Application.

It scrapes the Scrapy github pull requests data from https://github.com/scrapy/pulls

Taking advantage of Django Admin and some simple views to represent & visualize the data.

### Getting Started

Just clone the repository by typing in:

```bash
git clone https://github.com/nam4dev/web_scraping_presentation.git
```

###### Installation

**Only for Windows Users**, download [PostgreSQL](https://get.enterprisedb.com/postgresql/postgresql-11.4-1-windows-x64.exe) & Install it.
Open PgAdmin 
**Change Django Settings accordingly**

Install Python (3.7+)

[Create a python virtualenv](https://virtualenv.pypa.io/en/stable/installation/) in which you will install the requirements,

###### For Windows Users

[Installing Scrapy on Windows](https://docs.scrapy.org/en/latest/intro/install.html#windows)

###### For Linux Users

```bash
cd ./web_scraping_presentation
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Visualize modelled views (without data)

Open the web browser to http://127.0.0.1:8000/admin 

then login using credentials defined by the above command line (`createsuperuser`)

Go to Authors and Pull Requests sections in the Django admin zone to visualize tables.

Go on the root page http://127.0.0.1:8000 as well to visualize custom views without data.

### Fill database with scrapped data

It is now time to fill the database from the spider(s).

#### Through CLI

One can trigger the `github spider` by simply typing in a shell,

```bash
scrapy runspider web_crawlers/spiders/github.py
```

#### Through Django with scrapyd

##### Run scrapyd server

One can run the `scrapyd server` by simply typing in a shell,

```bash
cd web_scraping_presentation
scrapyd > scrapyd.server.log
```

##### Visualize scrapyd server interface

Go to http://127.0.0.1:6800

##### Deploy web_crawlers project to scrapyd server

**The scrapyd server shall run as prerequisite**

One can deploy the `web_crawlers project` by simply typing in a shell,

###### For Linux Users

```bash
cd web_scraping_presentation
scrapyd-deploy
```

###### For Windows Users
```bash
cd web_scraping_presentation
python setup.py bdist_egg
```

**Go on the root page http://127.0.0.1:8000, and click on the appropriated link: `Add the Github Spider Project to Scrapyd Server`**

##### Trigger Github Spider

**Go on the root page http://127.0.0.1:8000, and click on the appropriated link: `Trigger the Github Spider`**

#### Go further and automate it through celery

Just as an hint, one can easily automate by periodically scheduling a task to trigger the
spider(s) through [Celery](http://www.celeryproject.org/) Distributed Task Queue & [django-celery](https://github.com/celery/django-celery/) plugin for example

### Visualize scrapped data

Go back to Authors and Pull Requests sections in the Django admin zone to visualize scrapped data.

Go back on the root page http://127.0.0.1:8000 as well to visualize the data through custom views.

