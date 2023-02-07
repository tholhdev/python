import os
import requests

# try:
#     url_test = os.environ["url"]
# except KeyError:

url_test = os.environ['url']
x = requests.get('url_test')
print(x.status_code)