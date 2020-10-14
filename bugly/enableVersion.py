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
    # print(res)
    # for i in res:
    #     version = i["version"]
    #     displayversion_list.append(version)
    return res

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
        v = version["version"]
        if v not in not_enableVersion_list and version["isShow"] == True:
            set_url = "https://bugly.qq.com/v2/apps/81452cad5e/platformId/2/userId/9BC53E3B6045DD9F75394B209D29119B/isShow/false/enableVersion?version="+str(v)
            set = requests.get(url=set_url,headers=headers,cookies=cookie_dict).json()
            print(v)
        else:
            pass


def get_bugly_release_version():
    version_url = "https://raw.githubusercontent.com/demonnboy/img_folder/master/bugly/version.json"
    get_versions = requests.get(url=version_url).json()
    return get_versions
    

if __name__ == '__main__':

    cookie = "pgv_pvid=5588621980; tvfe_boss_uuid=1b261d545b29005c; RK=rNxwV09iUF; ptcz=ab258dcdf844b2b067031ff71c7df6d42d8fc3d69443e6fbbd06f63e305cf5c0; pgv_pvi=1726780416; o_cookie=409777183; pac_uid=1_409777183; ied_qq=o0409777183; eas_sid=S1W548Q3y3q163R6D8D9O905q1; _ga=GA1.2.1845725167.1594693096; btcu_id=876711e194caa4a523f06ffe6df4c1235f0d15e8234e4; vc=vc-f4038330-1bc4-44dc-b39e-d482e5514cd8; vc.sig=WhSZrxfVQHFt2UAH-MecQpOZLPqpOObXcPS4izcgryE; sd_userid=84341595339107335; sd_cookie_crttime=1595339107335; vc=vc-492d1911-c3fb-4ebd-ba85-7ff444c015ed; btcu_id=3f504319-6569-4f8c-9e3c-f28bc069db58; pgv_si=s3824227328; _gid=GA1.2.1172516661.1602384757; connect.sid=s%3ALoHznMgAnWvCUh04ZjSLGCw1Ppnz2ZtG.k6ODhlm4IKsllLM8Nj%2FsOhC28aN6Y5AUilbUkkSK7CU; token-skey=4dc0b389-2396-6af0-5ffb-ca9987606bde; token-lifeTime=1602597074; NODINX_SESS=PBi5rsxXthTfxazy-toe_4Jwwu-1bzaBzlBYEN1K9ytgEUHoQU1XGHmAnLg87zn6; csrfToken=CRL2-QnRZ4-u5QjBRAM-MThU; _gat=1; bugly_session=eyJpdiI6IkZURUpBY1RsMFk3RTU1dVY2Y0pEY1E9PSIsInZhbHVlIjoiZGlFNWVnMHBmSGxDVU9SNlUyMkZNVE1oN0lpVHBsWjI5bTk2a3E1dHFXdTlscElyMlQzWEVKM3VNOStwN1BLeTVXOENhN0hFRjBBUHBpWkZcL1VHamtBPT0iLCJtYWMiOiIzZDY2MDFiZTc1OTA3ZjYxNmQ5OGE1OWRlY2FjOTk5YmZhYWEwMWZkOTVlODc4ZDRlN2U1OGYyOWE2MmFiNzI1In0%3D; referrer=eyJpdiI6Ik5qbWRHTWtUSmt1MWpXSEE4dnFcLzJnPT0iLCJ2YWx1ZSI6IjVkTmlTTVFjXC91dW1KWTA1OWdiNmg0UERkZTVkUGVFM1wvUEZLY1MxVFwvd1wvWTRrS3RQUWk5WEVab0xDN3lrYkZhUVVkTXBXbWo3U1hIQWdqclZNbjRoU2liT1VZWTZJTXFJMWx5ZENGOEJJTT0iLCJtYWMiOiIxODkzNDdkNzc4MDE3YmI4NDY4NzdmNWQwMzQ2ZjU1ZWMxYjQ2NzkxNDVkMTNmZmVjNWY0N2YyYzMwY2ViOTk2In0%3D"
    x_csrf_token="CRL2-QnRZ4-u5QjBRAM-MThU"
    x_token="683835322"
    # not_enableVersion_list = get_displayversion(cookie,x_csrf_token,x_token)
    release_versions = get_bugly_release_version()
    set_enableVersion(cookie,x_csrf_token,x_token,release_versions)
