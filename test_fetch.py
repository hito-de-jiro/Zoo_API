import requests
import json


url_token = 'https://www.zooplus.de/tierarzt/api/v2/token?debug=authReduxMiddleware-tokenIsExpired'


# Отримує доступ до API
def fetch(url, params):
    headers = params["headers"]
    body = params["body"]
    session = requests.Session()
    res = session.get(url=url, headers=headers, data=body)
    print(res.status_code)
    json_data = json.loads(res.text)
    print(json_data)
    with open('json_data.json', 'w', encoding='utf-8') as f:
        f.write(res.text)


fetch("https://www.zooplus.de/tierarzt/api/v2/results?animal_99=true&page=1&from=0&size=20", {
    "headers": {
        "accept": "application/json",
        "accept-language": "en,en-US;q=0.9",
        "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NjQxMjM4ODksImlhdCI6MTY2NDEyMjk4OX0.dRZu6IJUTdHmlhvuhrMqtB90WWoSDYuBHFLc64OPl8o",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "sec-ch-ua": "\"Google Chrome\";v=\"105\", \"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"105\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-api-authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NjQxMjM4ODksImlhdCI6MTY2NDEyMjk4OX0.dRZu6IJUTdHmlhvuhrMqtB90WWoSDYuBHFLc64OPl8o",
        "x-site-id": "1",
        "cookie": "ctid_ch_adv_ss=1353727nn:0|1353727rn:0|1353727nn:0|1353727nn:0|1353727nn:0|1353727nn:0|1353727nn:0|1353727nn:0|1353727nn:0|1353727nn:0|1353727nn:0|1353727nn:0|1353727nn:0|1353727nn:0|1353727nn:0^1664122948868; sid=1b2e8300-d64b-49c6-af24-e254a2c8f0cf; OptanonAlertBoxClosed=2022-09-21T11:27:00.904Z; OneTrust_PerformanceCookies=YES; at_check=true; OneTrust_FunctionalCookies=YES; OneTrust_TargetingCookies=YES; AMCVS_BD7F317853C3F61D0A490D4E%40AdobeOrg=1; adb_MrktCloudId=92002251134904885903205350535397521603; s_pfs=%5B%5BB%5D%5D; s_cc=true; CHKSESSIONID=E224AFC2071A191A64C01E87E43B799D; _hjSessionUser_720363=eyJpZCI6ImEyNTVkNWVjLWM4ZDctNTQ5YS05Mjg3LTk2OWM4Yjc0OWEwMyIsImNyZWF0ZWQiOjE2NjM3NTk3NjYyMTksImV4aXN0aW5nIjpmYWxzZX0=; _gcl_au=1.1.1212011768.1663759767; zt_id=63e7b61e-c6df-425d-af1e-ce52eca1c8d7; ctid_ch_adv_ss=1353727nn:0|1353727rn:0^1663764349977; _hjSessionUser_720357=eyJpZCI6IjFiYWI5OWMwLTQ2OWUtNWYxOC04NDBkLThkYTUwZTMzMWQ2YSIsImNyZWF0ZWQiOjE2NjM3NjQzNTAxNjIsImV4aXN0aW5nIjp0cnVlfQ==; _fbp=fb.1.1663772799303.395981455; s_sq=%5B%5BB%5D%5D; _hjShownFeedbackMessage=true; AMCV_BD7F317853C3F61D0A490D4E%40AdobeOrg=-1124106680%7CMCIDTS%7C19261%7CMCMID%7C92002251134904885903205350535397521603%7CMCAAMLH-1664722334%7C6%7CMCAAMB-1664722334%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1664124734s%7CNONE%7CvVersion%7C5.2.0; s_ips=890; s_tp=890; _hjIncludedInPageviewSample=1; _hjIncludedInSessionSample=1; vetsearch.sid=s%3AmTgYtqbc6oTQFs1kjtsvH3FjMa4TXoMd.DPJ6vxHSuxKIriAbb15i5Jpj6FgWsmL8zHKsujdr7K4; ctid_chain=1353727|1353727|1353727|1353727|1353727|1353727|1353727|1353727|1353727|1353727|1353727|1353727|1353727|1353727|1353727; ctid_ch_adv=1353727:0|1353727:0|1353727:0|1353727:0|1353727:0|1353727:0|1353727:0|1353727:0|1353727:0|1353727:0|1353727:0|1353727:0|1353727:0|1353727:0|1353727:0; visit_ctid=1353727; s_vnum=1666351621315%26vn%3D21; s_invisit=true; s_lv_s=Less%20than%201%20day; _hjSession_720357=eyJpZCI6IjhhNjY2ZDBiLTIzMzgtNGM1Zi04OTE1LWMyYmMwNmFiYTUzYiIsImNyZWF0ZWQiOjE2NjQxMjI5NDkyNDgsImluU2FtcGxlIjp0cnVlfQ==; _hjAbsoluteSessionInProgress=1; mbox=PC#8a79379f291d40b4992b220c329fbf3f.37_0#1727367754|session#b1ceb4fe05cf424c9f3c483a6b880936#1664124814; s_getNewRepeat=1664122953840-Repeat; s_ppv=www.zooplus.de%2Ftierarzt%2Fresults%2C100%2C100%2C890%2C1%2C1; s_lv=1664122953845; OptanonConsent=isIABGlobal=false&datestamp=Sun+Sep+25+2022+19%3A22%3A34+GMT%2B0300+(%D0%92%D0%BE%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B0%D1%8F+%D0%95%D0%B2%D1%80%D0%BE%D0%BF%D0%B0%2C+%D0%BB%D0%B5%D1%82%D0%BD%D0%B5%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=6.9.0&hosts=&consentId=ec9ac15a-7fc6-421e-a055-8de8dda0cc39&interactionCount=1&landingPath=NotLandingPage&groups=1%3A1%2C2%3A1%2C3%3A1%2C4%3A1&geolocation=UA%3B18&AwaitingReconsent=false; s_plt=1.32; s_pltp=www.zooplus.de%2Ftierarzt%2Fresults",
        "Referer": "https://www.zooplus.de/tierarzt/results?animal_99=true",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    },
    "body": '',
    "method": "GET"
})

print(len('"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NjQxMjc3ODAsImlhdCI6MTY2NDEyNjg4MH0.WjvzozMlC0Wqe7Ldad6CGFgdWIBX5c0OyaxHs5FyZlc"'))
print(len('"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NjQxMjM4ODksImlhdCI6MTY2NDEyMjk4OX0.dRZu6IJUTdHmlhvuhrMqtB90WWoSDYuBHFLc64OPl8o"'))