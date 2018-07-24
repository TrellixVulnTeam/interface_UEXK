#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 22:09
# @Author  : Carewn
# @Software: PyCharm

import requests
import json
import time,os
import configparser
from Public.logger import Logger
from Public.get_api import GetApi

mylog = Logger(logger="Getlogin").getlog()


class Get_Login():

    def __init__(self,host):
        self.host = host

    def get_mp_login_interface(self):
        '''获取平台端token'''
        # config = configparser.ConfigParser()
        # path = os.path.dirname(os.path.abspath('.'))+'\config\config.ini'
        # config.read(path,encoding="utf-8-sig")
        mp_login_url = ''
        if self.host == 'CS':
            mp_login_url = GetApi('mp_test_host','mp_login','config.ini').main()
        else:
            mp_login_url = GetApi('mp_host', 'mp_login', 'config.ini').main()
        mp_pic_url = GetApi('mp_host','picture_list','config.ini').main()
        return mp_login_url,mp_pic_url

    def get_test_login_interface(self):
        '''获取商家端token'''
        config = configparser.ConfigParser()
        path = os.path.dirname(os.path.abspath('.'))+'\config\config.ini'
        config.read(path,encoding="utf-8-sig")
        mp_login_url = GetApi('test_host','test_login','config.ini').main()
        return mp_login_url

    def get_mp_token(self):
        url = self.get_mp_login_interface()[0]
        data = {}
        if self.host == 'CS':
            data = {
                "account":"ggbadmin",
                "pwd":"e10adc3949ba59abbe56e057f20f883e"
            }
        else:
            data = {
                "account": "ggbadmin",
                "pwd": "f5dcc5a7cabbafd8695480c0edb7b35a"
            }
        r = requests.post(url,data=data)
        token = r.json()['token']
        token = "Bearer "+token
        return token

    def get_test_token(self):
        url = self.get_test_login_interface()
        data = {
            "account": "18664309864",
            "pwd": "ac140f9e701766ea44ded4aac0fbee6a"
        }
        r = requests.post(url, data=data)
        token = r.json()['token']
        token = "Bearer " + token
        return token

    def get_C_token(self):
        url = GetApi('C_host','phone_login','config.ini').main()
        data = {
            "MERCHANTID_C": "81136",
            "channel_code": "81136",
            "channel_name": "GoGoBeauty",
            "deviceos": "11.2.6",
            "devices": "iOS",
            "imie": "",
            "login_merchant_id": "81136",
            "login_token": "",
            "mac_code": "0775FC62-B783-4301-BED8-BBD243D7EB3E",
            "osversion": "11.2.6",
            "password": "381ec9fbdfac2be30c73cf23598a8a7a",
            "telphone": "15818758705",
            "version": "1.2.20"
        }
        r = requests.post(url,data=data)
        try:
            if r.json()['status'] != '500':
                mylog.info('获取token成功.....')
                return r.json()['token']
        except Exception as e:
            mylog.error('获取token失败')
            return 1

    def get_picurl(self):
        url = self.get_mp_login_interface()[1]
        data = {
            "pageNumber": 1,
            "pageSize": 10,
            "range": [],
            "type": []
        }
        headers = {
            "Authorization": self.get_mp_token(),
        }
        r = requests.post(url, data=data, headers=headers)
        rs = r.json()
        return rs

if __name__  == '__main__':
    s = Get_Login()
    s.get_mp_token()
    #s.get_picurl()
