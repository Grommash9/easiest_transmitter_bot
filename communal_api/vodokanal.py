import requests
from requests.structures import CaseInsensitiveDict
from bs4 import BeautifulSoup

with requests.Session() as session:

    url = "https://billing.vodokanal.kharkov.ua/login"

    headers = CaseInsensitiveDict()
    headers[
        "Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
    headers["Accept-Encoding"] = "gzip, deflate, br"
    headers["Accept-Language"] = "ru-RU,ru;q=0.9"
    headers["Connection"] = "keep-alive"
    headers["Host"] = "billing.vodokanal.kharkov.ua"
    headers["sec-ch-ua"] = '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"'
    headers["sec-ch-ua-mobile"] = "?0"
    headers["sec-ch-ua-platform"] = '"Windows"'
    headers["Sec-Fetch-Dest"] = "document"
    headers["Sec-Fetch-Mode"] = "navigate"
    headers["Sec-Fetch-Site"] = "none"
    headers["Sec-Fetch-User"] = "?1"
    headers["Upgrade-Insecure-Requests"] = "1"
    headers[
        "User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"

    resp = requests.get(url, headers=headers)
    print(resp.headers['Set-Cookie'])
    print(resp.status_code)
    soup = BeautifulSoup(resp.content)
    mydivs = soup.find_all("meta", {"name": "csrf-token"})
    for dive in mydivs:
        print(dive['content'])
        code = dive['content'][:-2] + '%3D%3D'
        print(code)

    url = "https://billing.vodokanal.kharkov.ua/get-form-send-indications"
    headers = CaseInsensitiveDict()
    headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
    headers["Accept-Encoding"] = "gzip, deflate, br"
    headers["Accept-Language"] = "ru-RU,ru;q=0.9"
    headers["Cache-Control"] = "max-age=0"
    headers["Connection"] = "keep-alive"
    headers["Content-Length"] = "219"
    headers["Content-Type"] = "application/json"
    headers["Cookie"] = resp.headers['Set-Cookie']
    headers["Host"] = "billing.vodokanal.kharkov.ua"
    headers["Origin"] = "https://billing.vodokanal.kharkov.ua"
    headers["Referer"] = "https://billing.vodokanal.kharkov.ua/login"
    headers["sec-ch-ua"] = '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"'
    headers["sec-ch-ua-mobile"] = "?0"
    headers["sec-ch-ua-platform"] = '"Windows"'
    headers["Sec-Fetch-Dest"] = "document"
    headers["Sec-Fetch-Mode"] = "navigate"
    headers["Sec-Fetch-Site"] = "same-origin"
    headers["Sec-Fetch-User"] = "?1"
    headers["Upgrade-Insecure-Requests"] = "1"
    headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"


    data = {
        '_csrf-frontend=': code,
        'NoLoginForm[acc]=': 225859,
        'NoLoginForm[fam]=': '%D0%A1%D0%B0%D0%BB%D0%B0%D1%82%D0%BE%D0%B2%D0%B0',
        'check-button=': ''
    }


    resp = requests.post(url, headers=headers, json=data)

    print(resp.status_code)
    print(resp.text)
