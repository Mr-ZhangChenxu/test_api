# /usr/local/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021-03-27  10:15 上午
# @Author  : 张晨旭
# @IDE     : PyCharm
# @PROJECT : Test_Api
# @File    : base.py
import requests


class Base():
    def __init__(self):
        '''
        1、实例化Session()
        2、声明base_url
        3、获取token并存入Session().params
        '''
        self.s = requests.Session()
        self.base_url = "https://qyapi.weixin.qq.com/cgi-bin"
        self.s.params["access_token"] = self.get_token()

    def get_token(self):
        '''
        获取token凭证
        :param corpid:企业ID
        :param corpsecret:应用的凭证密钥
        :return:token值
        '''
        params = {
            "corpid" : "ww491558834d2ff0a1",
            "corpsecret" : "XifeGU1Ud2Sn8PQXIETGVOWAISwvyxNRjkzbcuU9xFA"
        }
        r = requests.get(f"{self.base_url}/gettoken", params=params)
        token = r.json()['access_token']
        return token

    def send(self, method, *args, **kwargs):
        '''
        封装发送请求方法
        :param method:请求方法
        :param args：非键值对的可变数量的参数列表
        :param kwargs:不定长度的键值对作为参数
        :return:
        '''
        if method == 0:
            # 发送get请求
            return self.s.request("GET", *args, **kwargs)
        elif method == 1:
            # 发送post请求
            return self.s.request("POST", *args, **kwargs)
