import requests

# Scrapyd API URL
scrapyd_url = 'http://your_scrapyd_server:6800'  # Replace with your Scrapyd server URL

# List of spiders to run
spiders = ['NewsSpider1Spider', 'NewsSpider2Spider', 'NewsSpider4Spider', 'NewsSpider5Spider', 'NewsSpider6Spider']

# Schedule each spider
for spider in spiders:
    data = {
        'project': 'your_project_name',  # Replace with your Scrapy project name
        'spider': spider,
    }
    response = requests.post(f'{scrapyd_url}/schedule.json', data=data)

    if response.status_code == 200:
        print(f'Spider {spider} scheduled successfully.')
    else:
        print(f'Failed to schedule spider {spider}.')