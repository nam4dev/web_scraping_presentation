import os
import sys
import scrapyd_api

scrapyd = scrapyd_api.ScrapydAPI()


def add_web_crawlers_project_to_scrapyd_server():
    rc = 0

    project = 'web_crawlers'
    egg_filename = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        'dist', 'web_crawlers-0.0.1-py3.7.egg'
    )
    try:
        with open(egg_filename, 'rb') as egg:
            spider_count = scrapyd.add_version(project, '0.0.1', egg)
            print('Added {} Spider to {}'.format(spider_count, project))
    except (OSError, IOError, Exception) as error:
        print(error, file=sys.stderr)
        rc = -1

    return rc


if __name__ == '__main__':
    exit(add_web_crawlers_project_to_scrapyd_server())
