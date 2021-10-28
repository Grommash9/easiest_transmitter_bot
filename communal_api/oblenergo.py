import requests
from requests.structures import CaseInsensitiveDict

url = "https://pa.oblenergo.kharkov.ua/frontend/web/index.php/site/login"

headers = CaseInsensitiveDict()
headers["authority"] = "pa.oblenergo.kharkov.ua"
headers["method"] = "POST"
headers["path"] = "/frontend/web/index.php/site/login"
headers["scheme"] = "https"
headers["accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
headers["accept-encoding"] = "gzip, deflate, br"
headers["accept-language"] = "ru-RU,ru;q=0.9"
headers["cache-control"] = "max-age=0"
headers["content-length"] = "269"
headers["Content-Type"] = "application/x-www-form-urlencoded"
headers["origin"] = "https://pa.oblenergo.kharkov.ua"
headers["referer"] = "https://pa.oblenergo.kharkov.ua/frontend/web/index.php/site/login"
headers["sec-ch-ua"] = '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"'
headers["sec-ch-ua-mobile"] = "?0"
headers["sec-ch-ua-platform"] = "'Windows'"
headers["sec-fetch-dest"] = "document"
headers["sec-fetch-mode"] = "navigate"
headers["sec-fetch-site"] = "same-origin"
headers["sec-fetch-user"] = "?1"
headers["upgrade-insecure-requests"] = "1"
headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"

data = """
LoginForm[email]: pavuk357@protonmail.com
LoginForm[password]: i9hYOMgdDVWVh6z5epDY
LoginForm[rememberMe]: 0
LoginForm[rememberMe]: 1
login-button: 
"""


resp = requests.post(url, headers=headers, data=data)

print(resp.status_code)

print(resp.text)