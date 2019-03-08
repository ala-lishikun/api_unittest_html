# -*- coding: utf-8 -*-
import requests
import  json
import conf.config
import test_case.Vehicle



def Get_token():
    c = conf.config.Config().get_conf()
    print(c)
    login_url = c["login_url"]
    username = c["uusername"]
    password = c["upassword"]
    data = {
        "username": username,
        "password": password
    }
    login_headers = {'Content-Type': 'application/json'}
    login_res = requests.post(url=login_url, json=data, headers=login_headers)
    token = login_res.headers["***-Auth-Token"]
    return token





def Get_Cookie():
    '''sem账号登录'''
    url = "***user_login"
    data = {
        "username": "test",
        "password": "6*****"
    }
    header = {'Content-Type': 'application/json'}
    login = requests.post(url, json=data, headers=header)
    coo = str(login.headers['Set-Cookie'])
    return coo.split(';')[0]




if __name__ == '__main__':
    print(Get_token())