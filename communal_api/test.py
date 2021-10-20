import requests
from requests.structures import CaseInsensitiveDict

url = "https://tftrade.net/app/load_inv"

headers = CaseInsensitiveDict()
headers["authority"] = "tftrade.net"
headers["method"] = "POST"
headers["path"] = "/app/load_inv"
headers["scheme"] = "https"
headers["accept"] = "*/*"
headers["accept-encoding"] = "gzip, deflate, br"
headers["accept-language"] = "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7"
headers["content-length"] = "32"
headers["Content-Type"] = "application/json"
headers["cookie"] = "_ga=GA1.1.1491922774.1634465436; sessionid=o9to8f7e8qu69s6fuc3d1cmoj5c7vqju; django_language=ru; currency=1; effects=0; paints=0; _ga_C8CQ8B8E6N=GS1.1.1634465435.1.1.1634465668.0"
headers["origin"] = "https://tftrade.net"
headers["referer"] = "https://tftrade.net/"
headers["sec-ch-ua"] = '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"'
headers["sec-ch-ua-mobile"] = "?0"
headers["sec-ch-ua-platform"] = '"Windows"'
headers["sec-fetch-dest"] = "empty"
headers["sec-fetch-mode"] = "cors"
headers["sec-fetch-site"] = "same-origin"
headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"

data = '{"who":"bots_all","update":true}'


items_list = requests.post(url, headers=headers, data=data)


with open('results.txt', 'w') as file_with_results:
    file_with_results.write(items_list.text)
