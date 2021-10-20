import requests
from requests.structures import CaseInsensitiveDict

url = "https://konto.onet.pl/newapi/oauth/email-user"

headers = CaseInsensitiveDict()
headers["authority"] = "konto.onet.pl"
headers["method"] = "POST"
headers["path"] = "/newapi/oauth/email-user"
headers["scheme"] = "https"
headers["accept"] = "application/json, text/plain, */*"
headers["accept-encoding"] = "gzip, deflate, br"
headers["accept-language"] = "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7"
headers["content-length"] = "1027"
headers["Content-Type"] = "application/x-www-form-urlencoded"
headers["cookie"] = ""
headers["origin"] = "https://konto.onet.pl"
headers["referer"] = "https://konto.onet.pl/"
headers["sec-ch-ua"] = '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"'
headers["sec-ch-ua-mobile"] = "?0"
headers["sec-ch-ua-platform"] = '"Windows"'
headers["sec-fetch-dest"] = "empty"
headers["sec-fetch-mode"] = "cors"
headers["sec-fetch-site"] = "same-origin"
headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"

data = {"login":"wdedasdas","domain":"op.pl","password":"TWQdsf23qeQ@#","name":"Vaele","surname":"SSsdd","place":"null","postal_code":"null","sex":"K","date_of_birth":"1976-03-21","agreements":["1","6","21","85"],"phone":"+48231232233","phone_token":"null","captcha_response":"","browser_params":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36","guardian_email":"","save_phone":True,"paid":False,"client_id":"poczta.onet.pl.front.onetapi.pl","recoveryEmail":""}


resp = requests.post(url, headers=headers, json=data)

print(resp.status_code)
print(resp.text)
for head, value in resp.headers.items():
    print(head, value)
