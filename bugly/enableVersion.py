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

    cookie = "pgv_pvid=5588621980; tvfe_boss_uuid=1b261d545b29005c; RK=rNxwV09iUF; ptcz=ab258dcdf844b2b067031ff71c7df6d42d8fc3d69443e6fbbd06f63e305cf5c0; pgv_pvi=1726780416; o_cookie=409777183; pac_uid=1_409777183; ied_qq=o0409777183; eas_sid=S1W548Q3y3q163R6D8D9O905q1; _ga=GA1.2.1845725167.1594693096; btcu_id=876711e194caa4a523f06ffe6df4c1235f0d15e8234e4; vc=vc-f4038330-1bc4-44dc-b39e-d482e5514cd8; vc.sig=WhSZrxfVQHFt2UAH-MecQpOZLPqpOObXcPS4izcgryE; sd_userid=84341595339107335; sd_cookie_crttime=1595339107335; vc=vc-492d1911-c3fb-4ebd-ba85-7ff444c015ed; btcu_id=3f504319-6569-4f8c-9e3c-f28bc069db58; pgv_info=ssid=s7884005171; pgv_si=s195227648; _gid=GA1.2.1582104179.1600586194; token-skey=d49b90d7-8398-a9b1-afd7-b7fd7b1e804d; token-lifeTime=1600965998; NODINX_SESS=n229DyzhLb0--dYeM0yWIqZ8EKUiNzVdxvuzd9lYbqZNA67_MFQpwckZOIxWtk2v; csrfToken=WkkLWsYZpi1NYm0Ay-fImbY1; _gat=1; bugly_session=eyJpdiI6IjA2WU5YOG94VTJ2b3JJNmQ4RWpQZmc9PSIsInZhbHVlIjoiWUlLVCttNisxQmVvNHZwRkh4Sk5NXC9uZDc4WTdTNWoxXC96MVUwTU5aNWV1YW1cL3M4M0FIbFo5QlorYkEwMUt5VFVScnk1QkJxR0tOMkszXC9tY01oTGZnPT0iLCJtYWMiOiIwZjY3YmNkMGE5NDAzNjEyMzQxODIwNTA2MDg2YWI4NDQ1MWEwNjhhYjkxMGU5ZTI0NDI1NjkxZTA0NGMzNWI3In0%3D; referrer=eyJpdiI6Iko1NlNtSkZ2VWtrdDFwTlBRTksza3c9PSIsInZhbHVlIjoiRWkzeDRISk10NUZ6NVJYOW93RTFMWjluOTk3RHJ4RnhSNGFXZXN0VXBCdUhDdGNLenpsZTQzcVNmYnI5N3pZZFJFaGI1WW9TS1BjSUVSSHNPSzlIMDNQUGZFWGMrdDBoR2JLNGU1VlRuYVE9IiwibWFjIjoiNGE5OWFiZWVmYWJmYjA4Njc3MTBjMjZiZWQ1ZjI4NmI5YTAzNmM2ZTg3NjM2Zjk5NzJmMjI4MjUwM2I1YjNkNSJ9"
    x_csrf_token="WkkLWsYZpi1NYm0Ay-fImbY1"
    x_token="393525581"
    # not_enableVersion_list = get_displayversion(cookie,x_csrf_token,x_token)
    release_versions = get_bugly_release_version()
    set_enableVersion(cookie,x_csrf_token,x_token,release_versions)
