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

    cookie = "pgv_pvid=5588621980; tvfe_boss_uuid=1b261d545b29005c; RK=rNxwV09iUF; ptcz=ab258dcdf844b2b067031ff71c7df6d42d8fc3d69443e6fbbd06f63e305cf5c0; pgv_pvi=1726780416; o_cookie=409777183; pac_uid=1_409777183; ied_qq=o0409777183; eas_sid=S1W548Q3y3q163R6D8D9O905q1; _ga=GA1.2.1845725167.1594693096; btcu_id=876711e194caa4a523f06ffe6df4c1235f0d15e8234e4; vc=vc-f4038330-1bc4-44dc-b39e-d482e5514cd8; vc.sig=WhSZrxfVQHFt2UAH-MecQpOZLPqpOObXcPS4izcgryE; sd_userid=84341595339107335; sd_cookie_crttime=1595339107335; vc=vc-492d1911-c3fb-4ebd-ba85-7ff444c015ed; btcu_id=3f504319-6569-4f8c-9e3c-f28bc069db58; pgv_info=ssid=s7884005171; pgv_si=s195227648; token-skey=57cfa243-e335-0fe0-06b0-dfc36e27e476; token-lifeTime=1600604193; NODINX_SESS=YfuS3QyYxPFKfuzQEd_Ljbj6pr1O6K3DZT8eMzhVjdIr5lojtHFzlKuNDszOkb8q; _gid=GA1.2.1582104179.1600586194; csrfToken=6UJd-nBSVj7TLi7OiiO5H5Ke; _gat=1; bugly_session=eyJpdiI6Ikp5Y1ZVMnJBVG9mSzR1dFo2dGNOXC93PT0iLCJ2YWx1ZSI6Iit4eG9nWE41dnFYK0xTaU9NK1dSek83XC84Q1VTUXNMS0NuZkVydjNBelcrcW1xOTFONGorblwvWmF6cWhyZ0E2c2E4WW82UkI0WDRQZWY4Y0RETkFTVGc9PSIsIm1hYyI6ImMxZjg1NWQ2MmJmMGU2OTJjZjhhZTEyNzMxMGIyMTMxY2FlNTIxNWNmYTFmMmI3N2IxZDc4NmFiNGY1NDJjNjYifQ%3D%3D; referrer=eyJpdiI6IkFSb05uYlltNGQxbUQ5N2ZwRk14TVE9PSIsInZhbHVlIjoiRlZFZGQyME1qTzZRTWhtZ2tzaUZRTkNxZk1JdllvdERiTkl1QmF5QWxzdXFDT3hmQzIrQm1ySXE2TzNtVk5BbkJrdERKZVFXTWpOSFBQRFwvM0ZYVFBJK04yeWVJWjRHT1hWK1IrZTl2cnJBPSIsIm1hYyI6ImQzMTJkM2FhMzM4YWIyZjk0ZmIxZTU3Yzc5ZGJhZjgwYzMzM2EwNTk1N2UxM2EzMjQ0NzNmZjNmNGFkYzQ1MDEifQ%3D%3D"
    x_csrf_token="6UJd-nBSVj7TLi7OiiO5H5Ke"
    x_token="1271460757"
    # not_enableVersion_list = get_displayversion(cookie,x_csrf_token,x_token)
    release_versions = get_bugly_release_version()
    set_enableVersion(cookie,x_csrf_token,x_token,release_versions)
