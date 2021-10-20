import time

import requests
from requests.structures import CaseInsensitiveDict
from urllib.parse import urlencode, quote_plus
from bs4 import BeautifulSoup

shitty_urlcoder = {
    'ё': '%B8',
    'ъ': '%FA',
    'ы': '%FB',
    'э': '%FD',
    'а': '%E0',
    'б': '%E1',
    'в': '%E2',
    'г': '%E3',
    'ґ': '%B4',
    'д': '%E4',
    'е': '%E5',
    'є': '%BA',
    'ж': '%E6',
    'з': '%E7',
    'и': '%E8',
    'і': '%B3',
    'ї': '%BF',
    'й': '%E9',
    'к': '%EA',
    'л': '%EB',
    'м': '%EC',
    'н': '%ED',
    'о': '%EE',
    'п': '%EF',
    'р': '%F0',
    'с': '%F1',
    'т': '%F2',
    'у': '%F3',
    'ф': '%F4',
    'х': '%F5',
    'ц': '%F6',
    'ч': '%F7',
    'ш': '%F8',
    'щ': '%F9',
    'ь': '%FC',
    'ю': '%FE',
    'я': '%FF'
}


def check_account(check_number, last_name):
    url = "https://www.hts.kharkov.ua/cabinet/login"

    headers = CaseInsensitiveDict()
    headers["authority"] = "www.hts.kharkov.ua"
    headers["method"] = "POST"
    headers["path"] = "/cabinet/login"
    headers["scheme"] = "https"
    headers[
        "accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
    headers["accept-encoding"] = "gzip, deflate, br"
    headers["accept-language"] = "ru-RU,ru;q=0.9"
    headers["cache-control"] = "max-age=0"
    headers["content-length"] = "42"
    headers["Content-Type"] = "application/x-www-form-urlencoded"
    headers["cookie"] = "cablang=u"
    headers["origin"] = "https://www.hts.kharkov.ua"
    headers["referer"] = "https://www.hts.kharkov.ua/cabinet/login"
    headers["sec-ch-ua"] = '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"'
    headers["sec-ch-ua-mobile"] = "?0"
    headers["sec-ch-ua-platform"] = '"Windows"'
    headers["sec-fetch-dest"] = "document"
    headers["sec-fetch-mode"] = "navigate"
    headers["sec-fetch-site"] = "same-origin"
    headers["sec-fetch-user"] = "?1"
    headers["upgrade-insecure-requests"] = "1"
    headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"

    encoded_second_name = ''
    for sym in last_name.lower():
        encoded_second_name += shitty_urlcoder[sym]

    data = f"rash={check_number}&lastn={encoded_second_name}&acc-signin="

    resp = requests.post(url, headers=headers, data=data)

    print(resp.status_code)
    x = str(resp.text).find('СТАН ОСОБОВОГО РАХУНКУ')
    return x


# print(check_account('517503943', 'Ким'))

def get_last_data(check_number, last_name):
    import requests
    from requests.structures import CaseInsensitiveDict

    payload = {'': f'{str(last_name).upper()}'}
    result = urlencode(payload, quote_via=quote_plus)

    url = f"https://www.hts.kharkov.ua/cabinet/hotwater/{check_number}/{result[1:]}"

    headers = CaseInsensitiveDict()
    headers["authority"] = "www.hts.kharkov.ua"
    headers["method"] = "GET"
    headers["path"] = "/cabinet/hotwater/517503943/%D0%9A%D0%98%D0%9C"
    headers["scheme"] = "https"
    headers[
        "accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
    headers["accept-encoding"] = "gzip, deflate, br"
    headers["accept-language"] = "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7"
    headers[
        "cookie"] = "LastLoginTabUsed=account; lang=u; _ga=GA1.3.953459482.1629972372; cablang=u; CABSESSID=618k600rgdir596mi4kcstgmv6"
    headers["referer"] = "https://www.hts.kharkov.ua/cabinet/517503943/%D0%9A%D0%98%D0%9C"
    headers["sec-ch-ua"] = '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"'
    headers["sec-ch-ua-mobile"] = "?0"
    headers["sec-ch-ua-platform"] = '""Windows""'
    headers["sec-fetch-dest"] = "document"
    headers["sec-fetch-mode"] = "navigate"
    headers["sec-fetch-site"] = "same-origin"
    headers["sec-fetch-user"] = "?1"
    headers["upgrade-insecure-requests"] = "1"
    headers[
        "user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"

    resp = requests.get(url, headers=headers)
    soup = BeautifulSoup(resp.text)
    mydivs = soup.find_all("td", {"class": "text-left"})
    answer = f'{mydivs[14].text[28:79]} {mydivs[15].text[28:79]}\n' \
             f'{mydivs[17].text[28:70]} {mydivs[18].text[28:79]}\n' \
             f'{mydivs[20].text[28:63]}: {mydivs[21].text[28:79]}'
    print(resp.status_code)
    return answer


def send_data(check_number, last_name, data):
    import requests
    from requests.structures import CaseInsensitiveDict

    payload = {'': f'{str(last_name).upper()}'}
    result = urlencode(payload, quote_via=quote_plus)

    url = f"https://www.hts.kharkov.ua/cabinet/hotwater/{check_number}/{result[1:]}"

    headers = CaseInsensitiveDict()
    headers["authority"] = "www.hts.kharkov.ua"
    headers["method"] = "POST"
    headers["path"] = "/cabinet/hotwater/517503943/%D0%9A%D0%98%D0%9C"
    headers["scheme"] = "https"
    headers[
        "accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
    headers["accept-encoding"] = "gzip, deflate, br"
    headers["accept-language"] = "ru-RU,ru;q=0.9"
    headers["cache-control"] = "max-age=0"
    headers["content-length"] = "77"
    headers["Content-Type"] = "application/x-www-form-urlencoded"
    headers["cookie"] = "LastLoginTabUsed=account; CABSESSID=o5bkud24t0ra8rb7at8mh7krl7; cablang=u"
    headers["origin"] = "https://www.hts.kharkov.ua"
    headers["referer"] = "https://www.hts.kharkov.ua/cabinet/hotwater/517503943/%D0%9A%D0%98%D0%9C"
    headers["sec-ch-ua"] = '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"'
    headers["sec-ch-ua-mobile"] = "?0"
    headers["sec-ch-ua-platform"] = '"Windows"'
    headers["sec-fetch-dest"] = "document"
    headers["sec-fetch-mode"] = "navigate"
    headers["sec-fetch-site"] = "same-origin"
    headers["sec-fetch-user"] = "?1"
    headers["upgrade-insecure-requests"] = "1"
    headers[
        "user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"

    data = f"0%5BValueN%5D={data}&send=%C7%E1%E5%F0%E5%E3%F2%E8+%EF%EE%EA%E0%E7%E0%ED%ED%FF"

    resp = requests.post(url, headers=headers, data=data)

    print(resp.status_code)

start_time = time.time()
print(get_last_data('517503943', 'Ким'))
print(time.time() - start_time)
