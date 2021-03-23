import requests, time
from multiprocessing import Pool


def send(no):
    cookies = {
    '__cfduid': 'de12be92f0e0fc2dcb4c96402a4d90a221605284220',
    'G_ENABLED_IDPS': 'google',
    'UserDidVisitApp': 'true',
    'language': 'en',
    'puntCookie': 'true',
    'PermissionPriming': '1',
    '__gads': 'ID=a512b20c3bb7bcbe:T=1605284267:S=ALNI_MY39QPrZVzhD3p5EQiZn_oibuf8oQ',
    'nativeBannerHidden': 'true',
    '_dd_l': '1',
    '_dd': '4f4ad111-1e6e-4c1b-85d4-b8efa76aae84',
    '__rtgt_sid': 'khgoyrxwc3cd07',
    'G_AUTHUSER_H': '1',
    'FirehoseSession-messaging': 'true',
    'connect.sid': 's%3AGICexqVA-7sZprgi4soC3bkUzFYkbXn3.ihoRd4J5B8w%2FIY5ecOkjrZ3YEbe0nMP%2FsdrGCTskAQM',
    'unsupported_browser': 'true',
    'unsupported_browsers_notif': 'true',
    'XSRF-TOKEN': 'G1uGqEkJ-ugYaaeMAYBmsyGL9WXYg_ifuxhE',
}

    headers = {
    'authority': 'www.textnow.com',
    'sec-ch-ua': '"Chromium";v="86", "\\"Not\\\\A;Brand";v="99", "Google Chrome";v="86"',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'x-csrf-token': 'XafOrYGm-R7oZgw54LVg_blMbXUcReSY2Oe0',
    'x-requested-with': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://www.textnow.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.textnow.com/messaging',
    'accept-language': 'en-US,en;q=0.9',
}


    text='Test'


    data = {
      'json': '{"contact_value":"+1'+no+'","contact_type":2,"message":"'+text+'","read":1,"message_direction":2,"message_type":1,"from_name":"","has_video":false,"new":true,"date":"2020-11-13T17:39:58.085Z"}'
    }

    response = requests.post('https://www.textnow.com/api/users/space027/messages', headers=headers, cookies=cookies, data=data)
    if response.status_code ==200:
        print('Sent ',no,response.text)
    else :
        print('Failed',response.text)

if __name__ == '__main__':
    TEXTList = open('nos.txt', 'r').read().splitlines()
    p = Pool(10)
    p.map(send, TEXTList)
    print('Finshed')
    time.sleep(5)
