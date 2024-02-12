import fake_useragent
import requests
from bs4 import BeautifulSoup

# url = ('https://github.com/login')
# response = requests.get(url)
# response_text = response.text
# # print(response_text)
#
# soup = BeautifulSoup(response_text, 'lxml')
# block = soup.find('div', {'class': 'auth-form-body mt-3'}).find('input',{'type':'hidden'} )
#
# print(block.get('value'))
# Вытягивали значение

user = fake_useragent.UserAgent().random
headers = {
    'user-agent': user
}
url_page = 'https://github.com/login'
url_auth = 'https://github.com/session'

data = {
    'login' : 'Legionaire25',
    'password': '230688bdb',
    'authenticity_token': ''
}

with requests.Session() as session:
    response = session.get(url_page, headers=headers)
    login_page_html = response.text
    print(response)

    soup = BeautifulSoup(login_page_html, 'lxml')
    block_token = soup.find('input', {'name': 'authenticity_token'})
    token = block_token.get('value')
    print(token)
    data['authenticity_token'] = token
    response = session.post(url_auth, headers=headers, data=data)
    result = response.text

with open('auth_page.html', 'w', encoding='utf-8') as file:
    file.write(result)





