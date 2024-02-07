import requests
import result

url = 'https://google-translate1.p.rapidapi.com/language/translate/v2/languages'
headers = {
    'Accept-Encoding': 'application/gzip',
    'X-RapidAPI-Key': '63e00ece09msh0c2cf4f9d39d433p1c0d87jsnef82f49514de',
    'X-RapidAPI-Host': 'google-translate1.p.rapidapi.com'
}
params = {'target': 'ru'}
response = requests.get(url, headers=headers, params=params)
print(response.status_code)
print(response.json())

url = "https://google-translate1.p.rapidapi.com/language/translate/v2/detect"
headers = {
"content-type": "application/x-www-form-urlencoded",
	"Accept-Encoding": "application/gzip",
	"X-RapidAPI-Key": "63e00ece09msh0c2cf4f9d39d433p1c0d87jsnef82f49514de",
	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
}
payload = { "q": "English is hard, but detectably so" }
response = requests.post(url, headers=headers, data=payload)
language = result["data"]["detections"][0][0]['language']
result = response.json()
a=0
print(f'{payload["q"]} - данная строка написана на {language}')