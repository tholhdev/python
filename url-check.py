import os
import requests

# try:
#     url_test = os.environ["url"]
# except KeyError:

url_test = os.environ['url']
y='http://' + url_test
print(y)
x = requests.get(y)
print(x.status_code)