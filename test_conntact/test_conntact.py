# /usr/local/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021-03-25  5:51 下午
# @Author  : 张晨旭
# @IDE     : PyCharm
# @PROJECT : Test_Api
# @File    : test_conntact.py
import requests


def get_token():
    r = requests.get(
        "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww491558834d2ff0a1&corpsecret=XifeGU1Ud2Sn8PQXIETGVOWAISwvyxNRjkzbcuU9xFA")
    token = r.json()["access_token"]
    return token

def test_get_member():
    get_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={get_token()}&userid=a001"
    r =requests.get(get_member_url)
    print(r)
    print(r.json())

def test_update_member():
    update_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={get_token()}"
    data = {
        "userid": "a001",
        "name": "李四",
    }
    r = requests.post(url=update_member_url, json=data)
    print(r.json())

def test_del_member():
    del_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={get_token()}&userid=root"
    r = requests.get(del_member_url)
    print(r.json())

def test_add_member():
    add_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={get_token()}"
    data = {
        "userid": "zhangsan",
        "name": "张三",
        "mobile": "13800000000",
        "department": [1],
    }
    r = requests.post(url=add_member_url, json=data)
    print(r.json())