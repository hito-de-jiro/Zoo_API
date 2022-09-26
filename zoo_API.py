import requests
import json


sess = requests.Session()
page = 1

api_url = 'https://www.zooplus.de/tierarzt/api/v2/token?debug=authReduxMiddleware-tokenIsExpired'
api_headers = {
    "accept": "application/json",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}
res_api = sess.get(url=api_url, headers=api_headers)
api_token = json.loads(res_api.text)

url = f"https://www.zooplus.de/tierarzt/api/v2/results?animal_99=true&page={str(page)}&from=0&size=20"
headers = {
    "accept": "application/json",
    "accept-encoding": "gzip, deflate, br",
    "authorization": f"Bearer {api_token['token']}",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "x-api-authorization": f"{api_token['token']}"
}

res = sess.get(url=url, headers=headers)
print(res.status_code)
print(res.text)

data_json = json.loads(res.text)
print(data_json)
# with open('json_data.json', 'w', encoding='utf-8') as f:
#     f.write(res.text)
name = data_json['result']['name']
print(name)