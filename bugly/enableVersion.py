# -*- coding: utf-8 -*

import requests

def get_displayversion(cookie,x_csrf_token,x_token):

    cookie = cookie
    x_csrf_token = x_csrf_token
    x_token = x_token
    cookie_dict = {i.split("=")[0]: i.split("=")[-1] for i in cookie.split("; ")}
    displayversion_list = []

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
        'Content-Type': 'application/json; charset=utf-8',
        'x-csrf-token': x_csrf_token,
        'X-token': x_token,
    }
    displayversion_url = "https://bugly.qq.com/v2/versions/appId/81452cad5e/platformId/2?needAll=true&fsn=9464ddda-e955-4545-b42d-24b97d0855c6"

    get_displayversion = requests.get(url=displayversion_url,headers=headers,cookies=cookie_dict).json()
    res  = get_displayversion["ret"]["versions"]
    print(res)
    for i in res:
        version = i["version"]
        displayversion_list.append(version)
    return displayversion_list

def set_enableVersion(cookie,x_csrf_token,x_token,not_enableVersion_list):
    cookie = cookie
    x_csrf_token = x_csrf_token
    x_token = x_token
    cookie_dict = {i.split("=")[0]: i.split("=")[-1] for i in cookie.split("; ")}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
        'Content-Type': 'application/json; charset=utf-8',
        'x-csrf-token': x_csrf_token,
        'X-token': x_token,
    }
    version_list = get_displayversion(cookie,x_csrf_token,x_token)
    for version in version_list:
        if version not in not_enableVersion_list:
            set_url = "https://bugly.qq.com/v2/apps/81452cad5e/platformId/2/userId/9BC53E3B6045DD9F75394B209D29119B/isShow/false/enableVersion?version="+str(version)
            set = requests.get(url=set_url,headers=headers,cookies=cookie_dict).json()
            print(version+"")
        else:
            pass


def get_bugly_release_version():
    version_url = "https://raw.githubusercontent.com/demonnboy/img_folder/master/version.json"
    get_versions = requests.get(url=version_url).json()
    return get_versions
    

if __name__ == '__main__':

    cookie = "pgv_pvid=5588621980; tvfe_boss_uuid=1b261d545b29005c; RK=rNxwV09iUF; ptcz=ab258dcdf844b2b067031ff71c7df6d42d8fc3d69443e6fbbd06f63e305cf5c0; pgv_pvi=1726780416; o_cookie=409777183; pac_uid=1_409777183; ied_qq=o0409777183; eas_sid=S1W548Q3y3q163R6D8D9O905q1; _ga=GA1.2.1845725167.1594693096; btcu_id=876711e194caa4a523f06ffe6df4c1235f0d15e8234e4; vc=vc-f4038330-1bc4-44dc-b39e-d482e5514cd8; vc.sig=WhSZrxfVQHFt2UAH-MecQpOZLPqpOObXcPS4izcgryE; sd_userid=84341595339107335; sd_cookie_crttime=1595339107335; vc=vc-492d1911-c3fb-4ebd-ba85-7ff444c015ed; btcu_id=3f504319-6569-4f8c-9e3c-f28bc069db58; pgv_info=ssid=s7884005171; pgv_si=s195227648; _gid=GA1.2.1923620191.1600050148; NODINX_SESS=puEWKqe0q8NJFsN87e71WBEUj6akDxePykp_FrC69mkJC95wgal5e8XmcqNBbFDJ; token-skey=5314362a-7df5-fd2d-d221-c7b96841c243; token-lifeTime=1600094990; csrfToken=E3rLrTC0RA7vU2svf7Eq0e0G; _gat=1; bugly_session=eyJpdiI6IjE3TXhxRVkxcFhLWWRcLzZydHp3WmpnPT0iLCJ2YWx1ZSI6IjF2Z3RtOXYxMzVjWGNWWnBrQ3h2M2tNZFVpeElodzhoZ0Rtc1Nqa0FadzVOd2xyd3ZEWDNjbmJ1S0dJMTQ1bEdoQWJDR1AzS3JQSWZONXlEQ0EwaUp3PT0iLCJtYWMiOiIzMTU1YjUwNjA0YWM5ZTlhOTJjZWU1ZWEwMTU5NTM3NDgxMTczMDJlMjMyMDBlZTM3MGQ5NTIyZmM4OTIwZGNmIn0%3D; referrer=eyJpdiI6IkZEbG52enI3dW5NVGxYU0dYa0lmUVE9PSIsInZhbHVlIjoiY2FSSlRQdkhhTTJEekk1dUxcL3dYWEw3cDZrdVdOY1Rja2l2RUIwQXJ2R0ZkWVV2a0pXRnphME9ENkRpSXdKOTduVDlBclVjXC9LUFwvRkloUkc3eUx3V0xVVzRkOEcxYmh2MDBBM0VpbllVMWZoR2ZOT1wvZ3JjNHh6SmsrVXlka01CRFdZNThnZ2srMm1mNzhYbzNHeDhWZmNHZjU3YWh6cXdFVGdxWDVxblh1dz0iLCJtYWMiOiI1MGMzNTQ3YjNmMWM1YjE5OGY5ZmFiNzI1NjcxY2EzYjI5MDg5ZjVmMmViYWQ0YzY4M2ZiOWIxNTZjODczNDdjIn0%3D"
    x_csrf_token="E3rLrTC0RA7vU2svf7Eq0e0G"
    x_token="594048373"
    # not_enableVersion_list = get_displayversion(cookie,x_csrf_token,x_token)
    release_versions = get_bugly_release_version()
    set_enableVersion(cookie,x_csrf_token,x_token,release_versions)
