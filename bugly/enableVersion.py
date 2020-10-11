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

    cookie = "pgv_pvid=5588621980; tvfe_boss_uuid=1b261d545b29005c; RK=rNxwV09iUF; ptcz=ab258dcdf844b2b067031ff71c7df6d42d8fc3d69443e6fbbd06f63e305cf5c0; pgv_pvi=1726780416; o_cookie=409777183; pac_uid=1_409777183; ied_qq=o0409777183; eas_sid=S1W548Q3y3q163R6D8D9O905q1; _ga=GA1.2.1845725167.1594693096; btcu_id=876711e194caa4a523f06ffe6df4c1235f0d15e8234e4; vc=vc-f4038330-1bc4-44dc-b39e-d482e5514cd8; vc.sig=WhSZrxfVQHFt2UAH-MecQpOZLPqpOObXcPS4izcgryE; sd_userid=84341595339107335; sd_cookie_crttime=1595339107335; vc=vc-492d1911-c3fb-4ebd-ba85-7ff444c015ed; btcu_id=3f504319-6569-4f8c-9e3c-f28bc069db58; pgv_info=ssid=s7884005171; pgv_si=s195227648; _gid=GA1.2.1120582310.1601171521; token-skey=5f9de032-4706-6bc6-265a-fbdac34ecd23; token-lifeTime=1601383584; NODINX_SESS=L4w-89TNFNXKTFRAq7WpTMrcT988KPq2ftFDu6EB6Z1Pl3rCs7bi6t__Q3DSTGEk; csrfToken=wf-4jHI_-Iuzr3Vl0TBAXo8r; _gat=1; bugly_session=eyJpdiI6Ildqb1FGc2J5cWw3TjVcL2RhdnA1K3pBPT0iLCJ2YWx1ZSI6IjRzK3YwYlNGTnBmdEsrVjlcLzFDZ2NwZFhOcys3eTZtMkhMWnpGTFwvbXF2UTBjUWphSDladVpTdFd5ak1vUGVqUDVLM0czcCtPM28xSkNhclFQMjd4S0E9PSIsIm1hYyI6IjRmZjM0YTY5NmQxZTc2YTFjZWY0YmQ2NzgyNzc5NGU0NzMxNDdmZjJkYmZlZmRjMzMwYjY2NDNmZWJhZjgzNzYifQ%3D%3D; referrer=eyJpdiI6ImlxRUVpb1VidjlvVG9wbDdNcjZuTFE9PSIsInZhbHVlIjoiTml1NU5ib1RJYnR0d01QaDk4V29kbmZUUUJVSmNrT1pYdjZTQVdwazJsN2VGSFZrUlMrbmlVdVduSlZxUmhjTGJhdFRwV2ozMHU0S044Z1V4VDhMUjM4NzNnOUM3RGZxU2hNczNpM0RnQlgxXC9MNUJlMWdybjJqWjdpYWllYXpOY3ppRjZVcUU4MjJGZjdMam9MVEtCNXNtXC9oQkFQT3hIVlREMFNabVlEa1U9IiwibWFjIjoiYzgyMDgxYzVjNDI1NzlkMTZkZTUxYTQ3ODBkOWM3NzQ5MTMzNjJhNGZkMWYzOTJiZmE4MDI4ZmVkNmFhMzMyZCJ9"
    x_csrf_token="wf-4jHI_-Iuzr3Vl0TBAXo8r"
    x_token="1050881907"
    # not_enableVersion_list = get_displayversion(cookie,x_csrf_token,x_token)
    release_versions = get_bugly_release_version()
    set_enableVersion(cookie,x_csrf_token,x_token,release_versions)
