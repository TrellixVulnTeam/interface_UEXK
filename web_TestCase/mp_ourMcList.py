#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 14:05
# @Author  : Carewn
# @Software: PyCharm


import requests,json,os,time
from Public.logger import Logger
from Public.get_api import GetApi
from Public.Get_login_token import Get_Login
import threading

mylog = Logger(logger='mp_log').getlog()
class mp_ourmclist():

    def __init__(self):
        try:
            self.token = Get_Login().get_mp_token()
            mylog.info('token获取成功......')
        except Exception as e:
            mylog.error('token获取失败')
            print (self.token)
            raise ValueError(e)

        self.HJ = 'CS'
        if self.HJ == 'CS':
            self.mini_url = GetApi('mp_test_host', 'mp_mini_list','config.ini').main()
            self.Code_url = GetApi('mp_test_host','mp_Code','config.ini').main()
            self.commit_url = GetApi('mp_test_host','mp_commit_code','config.ini').main()
            self.cate_url = GetApi('mp_test_host','mp_wx_cate','config.ini').main()
            self.commitSh = GetApi('mp_test_host','mp_commitSh','config.ini').main()
        else:
            self.mini_url = GetApi('mp_host', 'mp_mini_list', 'config.ini').main()
            self.Code_url = GetApi('mp_host', 'mp_Code', 'config.ini').main()
            self.commit_url = GetApi('mp_host', 'mp_commit_code', 'config.ini').main()
            self.cate_url = GetApi('mp_host', 'mp_wx_cate', 'config.ini').main()
            self.commitSh = GetApi('mp_host', 'mp_commitSh', 'config.ini').main()

        self.get_request = self.get_request()
        self.code = self.get_code()

    def get_request(self):
        data = {
            'pageNumber':1,
            'pageSize':100,
            'status':2
        }
        r = requests.post(self.mini_url,data)
        our_app = []
        for i in r.json()['data']:
            one_app = []
            one_app.append(i['appid'])
            one_app.append(i['name'])
            one_app.append(i['tradeRole'])
            one_app.append(i['merchantid_c'])
            our_app.append(one_app)
        mylog.info('获取所有小程序信息成功......')
        return our_app


    #根据小程序的appid获取所有模板,并取最新的一个
    def get_code(self):
        r = ''
        data = {
            'appid':self.get_request[0][0]
        }
        try:
            r = requests.post(self.Code_url,data)
        except Exception as e:
            mylog.error('获取模板失败')
        template_id = ''
        user_version = ''
        user_desc = ''
        template_id = 0
        for i in r.json()['data']['template_list']:
            if i['template_id'] > template_id:
                template_id = i['template_id']
                user_version = i['user_version']
                user_desc = i['user_desc']
        mylog.info('获取最新模板信息成功.......')
        return template_id,user_version,user_desc

    #提交模板
    def commitCode(self,i):
        data = {}
        r = ''
        if i[2] == 1:
            i[2] = True
        else:
            i[2] = False
        data = {
            'appid':i[0],
            'merchant_name':i[1],
            'tradeRole':i[2],
            'merchantid_c':i[3],
            'templateId':self.code[0],
            'userDesc':self.code[2],
            'userVersion':self.code[1]
        }
        try:
            r = requests.post(self.commit_url,json=data)
        except Exception as e:
            mylog.error('{}模板设置失败'.format(data['merchant_name']))
        if r.json()['msg'] == '操作成功':
            mylog.info('{}模板操作成功,模板名称{}'.format(data['merchant_name'],data['userDesc']))
        else:
            mylog.error('{}操作失败,失败原因{}'.format(data['merchant_name'],r.json()))

    def cateAndcommit(self,i,data):
        try:
            headers = {
                'Authorization':self.token
            }
            datas = {
                'appid':i[0],
                'itemList':[data]
            }
            r = requests.post(self.commitSh,json=datas,headers=headers)
            if r.json()['msg'] == '操作成功':
                mylog.info('{}提交成功'.format(i[1]))
            else:
                mylog.error('{}提交失败'.format(i[1]))
        except Exception as e:
            mylog.error('----到{}报错啦报错啦!!!!!!!!!!!!----'.format(i[1]))

    def commit(self):
        ourThread = []
        for i in self.get_request:
            a = threading.Thread(target=self.commitCode,args=(i,))
            a.setDaemon(True)
            ourThread.append(a)

        for i in ourThread:
            i.start()

        for i in ourThread:
            i.join()

    def commitour(self):
        ourThread = []
        data = {}
        r = requests.post(self.cate_url, data={'appid': self.get_request[1][0]})
        cate = r.json()['category_list']
        for i in cate:
            if i['third_class'] == '美容':
                data['address'] = 'pages/index/index'
                data['first_class'] = i['first_class']
                data['first_id'] = i['first_id']
                data['second_class'] = i['second_class']
                data['second_id'] = i['second_id']
                data['third_class'] = i['third_class']
                data['third_id'] = i['third_id']
                data['title'] = '首页'
                continue
        for i in self.get_request:
            a = threading.Thread(target=self.cateAndcommit,args=(i,data))
            a.setDaemon(True)
            ourThread.append(a)

        for i in ourThread:
            i.start()

        for i in ourThread:
            i.join()


if __name__ == "__main__":
    x = mp_ourmclist().commit()
    y = mp_ourmclist().commitour()


