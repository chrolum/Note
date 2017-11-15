import requests
import json


playload = {'some': 'data'}
url = 'https://api.github.com/some/endpoint'
r = requests.post(url, data=json.dumps(playload))
files = {'file': ('report.csv')}
print(r.)
