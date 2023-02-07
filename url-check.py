import os
import requests

# try:
#     url_test = os.environ["url"]
# except KeyError:

url_test = os.environ['url']
print('http://url_test')
x = requests.get('http://url_test')
print(x.status_code)