import requests
from bs4 import BeautifulSoup

# data = {
#     "name": "Apple MacBook Pro 16",
#     "data": {
#         "year": 2019,
#         "price": 1849.99,
#         "CPU model": "Intel Core i9",
#         "Hard disk size": "1 TB"
#     }
# }
# response = requests.post('http://api.restful-api.dev/objects', json=data)
# print(response.headers)
response = requests.get('http://www.onliner.by')
html_onliner = response.text

soup = BeautifulSoup(html_onliner, 'lxml')
links = soup.find_all('a')
for link in links:
    print(link.get('href'))
