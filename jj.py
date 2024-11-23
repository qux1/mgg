print('''
==========================================
|       [Report Story Instagram]              
|    [developer] => : M3GON               
|    [Channel Telegram] => : @M3GONPY  
|    [insta] => : _m3gon                  
==========================================
''')
try:
    import requests
    import time
except:
    print('[-] pip install requests')
    exit(0)
username_login = input('[+] Enter Username To Login in Instagram : ')
password_login = input('[+] Enter Password : ')
url_login = 'https://www.instagram.com/accounts/login/ajax/'
headers_login = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-length': '291',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'ig_did=3E70DB93-4A27-43EB-8463-E0BFC9B02AE1; mid=YCAadAALAAH35g_7e7h0SwBbFzBt; ig_nrcb=1; csrftoken=COmXgzKurrq8awSnRS1xf3u9rL6QsGZI',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
    'x-csrftoken': 'COmXgzKurrq8awSnRS1xf3u9rL6QsGZI',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': '1cb44f68ffec',
    'x-requested-with': 'XMLHttpRequest'
}
data_login = {
    'username': username_login,
    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1613414957:{password_login}',
    'queryParams': '{}',
    'optIntoOneTap': 'false'
}
req_login = requests.post(url_login, data=data_login, headers=headers_login)
if '"authenticated":false' in req_login.text:
    print('[!] Username Or Password Is Error - Try Agin')
    exit(0)
elif '"authenticated":true' in req_login.text:
    print('[+] Done Login')
    sessd = req_login.cookies['sessionid']
    self = 0
    error = 0
    spam = 0
    errorspam = 0
    heat = 0
    errorheat = 0
    url_story = input('[+] Enter Id Story : ')
    sleepo = int(input('[+] Enter Sleep : '))
    print('====================================')
    url = 'https://www.instagram.com/reports/web/get_frx_prompt/'
    headers = {
        'Connection': 'close',
        'Content-Length': '3048',
        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        'X-IG-WWW-Claim': 'hmac.AR22Czu8-j8I5M_o25CdmCD-zZ7gUJlWLRnUeUUz5S2SZymP',
        'sec-ch-ua-mobile': '?0',
        'X-Instagram-AJAX': '6d90752528fc',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': '*/*',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
        'X-CSRFToken': 'sZV3yutb0zM3AdnNsroVT9Z2TS4D9Nwq',
        'X-IG-App-ID': '936619743392459',
        'Origin': 'https://www.instagram.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': f'https://www.instagram.com/stories/therock/{url_story}/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cookie': f'ig_did=C9D6B8FE-134F-49E5-A1E7-547A96C68F2E; mid=YD8WNwALAAFzfOVEzjiWCPK1epjS; ig_nrcb=1; fbm_124024574287414=base_domain=.instagram.com; csrftoken=sZV3yutb0zM3AdnNsroVT9Z2TS4D9Nwq; ds_user_id=46629315319; sessionid={sessd}; rur=FTW'#m3gon
    }
    data = {
        'entry_point': '1',
        'location': '4',
        'object_type': '1',
        'object_id': f'{url_story}',
        'container_module': 'StoriesPage',
        'frx_prompt_request_type': '1'
    }
    req = requests.post(url, data=data, headers=headers)
    contet = str(req.json()['response']['context'])
    url2 = 'https://www.instagram.com/reports/web/get_frx_prompt/'
    headers2 = {
        'Connection': 'close',
        'Content-Length': '3048',
        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        'X-IG-WWW-Claim': 'hmac.AR22Czu8-j8I5M_o25CdmCD-zZ7gUJlWLRnUeUUz5S2SZymP',
        'sec-ch-ua-mobile': '?0',
        'X-Instagram-AJAX': '6d90752528fc',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': '*/*',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
        'X-CSRFToken': 'sZV3yutb0zM3AdnNsroVT9Z2TS4D9Nwq',
        'X-IG-App-ID': '936619743392459',
        'Origin': 'https://www.instagram.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': f'https://www.instagram.com/stories/therock/{url_story}/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cookie': f'ig_did=C9D6B8FE-134F-49E5-A1E7-547A96C68F2E; mid=YD8WNwALAAFzfOVEzjiWCPK1epjS; ig_nrcb=1; fbm_124024574287414=base_domain=.instagram.com; csrftoken=sZV3yutb0zM3AdnNsroVT9Z2TS4D9Nwq; ds_user_id=46629315319; sessionid={sessd}; rur=FTW'
    }
    data2 = {
        'entry_point': '1',
        'location': '4',
        'object_type': '1',
        'object_id': url_story,
        'container_module': 'StoriesPage',
        'context': contet,
        'action_type': '2',
        'frx_prompt_request_type': '4'
    }
    while True:
        req2 = requests.post(url2, data=data2, headers=headers2).text
        if '"status":"ok"' in req2:
            self += 1
            print(f'[+] Done Self With Story - {self}')
            time.sleep(sleepo)
        else:
            error += 1
            print(f'[-] Error Self With Story - {error}')
        url3 = 'https://www.instagram.com/reports/web/get_frx_prompt/'
        headers3 = {
            'Connection': 'close',
            'Content-Length': '3048',
            'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
            'X-IG-WWW-Claim': 'hmac.AR22Czu8-j8I5M_o25CdmCD-zZ7gUJlWLRnUeUUz5S2SZymP',
            'sec-ch-ua-mobile': '?0',
            'X-Instagram-AJAX': '6d90752528fc',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': '*/*',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
            'X-CSRFToken': 'sZV3yutb0zM3AdnNsroVT9Z2TS4D9Nwq',
            'X-IG-App-ID': '936619743392459',
            'Origin': 'https://www.instagram.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': f'https://www.instagram.com/stories/therock/{url_story}/',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cookie': f'ig_did=C9D6B8FE-134F-49E5-A1E7-547A96C68F2E; mid=YD8WNwALAAFzfOVEzjiWCPK1epjS; ig_nrcb=1; fbm_124024574287414=base_domain=.instagram.com; csrftoken=sZV3yutb0zM3AdnNsroVT9Z2TS4D9Nwq; ds_user_id=46629315319; sessionid={sessd}; rur=FTW'#m3gon
        }
        data3 = {
            'entry_point': '1',
            'location': '4',
            'object_type': '1',
            'object_id': url_story,
            'container_module': 'StoriesPage',
            'context': contet,
            'selected_tag_types': '["ig_spam_v3"]',
            'frx_prompt_request_type': '2'
        }
        reqspam = requests.post(url3, data=data3, headers=headers3).text
        if '"status":"ok"' in reqspam:
            spam +=1
            print(f'[+] Done Spam With Story - {spam}')
            time.sleep(sleepo)
        else:
            errorspam +=1
            print(f'[-] Error Spam With Story - {errorspam}')
        url4 = 'https://www.instagram.com/reports/web/get_frx_prompt/'
        headers4 = {
            'Connection': 'close',
            'Content-Length': '3048',
            'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
            'X-IG-WWW-Claim': 'hmac.AR22Czu8-j8I5M_o25CdmCD-zZ7gUJlWLRnUeUUz5S2SZymP',
            'sec-ch-ua-mobile': '?0',
            'X-Instagram-AJAX': '6d90752528fc',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': '*/*',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
            'X-CSRFToken': 'sZV3yutb0zM3AdnNsroVT9Z2TS4D9Nwq',
            'X-IG-App-ID': '936619743392459',
            'Origin': 'https://www.instagram.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': f'https://www.instagram.com/stories/therock/{url_story}/',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cookie': f'ig_did=C9D6B8FE-134F-49E5-A1E7-547A96C68F2E; mid=YD8WNwALAAFzfOVEzjiWCPK1epjS; ig_nrcb=1; fbm_124024574287414=base_domain=.instagram.com; csrftoken=sZV3yutb0zM3AdnNsroVT9Z2TS4D9Nwq; ds_user_id=46629315319; sessionid={sessd}; rur=FTW'
        }
        data4 = {
            'entry_point': '1',
            'location': '4',
            'object_type': '1',
            'object_id': url_story,
            'container_module': 'StoriesPage',
            'context': contet,
            'action_type': '2',
            'frx_prompt_request_type': '4'
        }
        reqhate = requests.post(url4, data=data4, headers=headers4).text
        if '"status":"ok"' in reqspam:
            heat +=1
            print(f'[+] Done Hate With Story - {heat}')
            time.sleep(sleepo)
        else:
            errorheat +=1
            print(f'[-] Error Hate With Story - {errorheat}')
