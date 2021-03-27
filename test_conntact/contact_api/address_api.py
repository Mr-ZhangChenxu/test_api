# /usr/local/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021-03-27  10:50 上午
# @Author  : 张晨旭
# @IDE     : PyCharm
# @PROJECT : Test_Api
# @File    : address_api.py
from test_conntact.contact_api.base import Base


class AddressApi(Base):
    '''
    通讯录管理接口
    '''
    def create_member(self, user_id, name, mobile, department):
        '''
        # 调用创建成员接口,POST请求
        :param user_id:成员UserID。对应管理端的帐号，企业内必须唯一
        :param name:成员名称。
        :param mobile:手机号码。企业内必须唯一，mobile/email二者不能同时为空
        :param department:成员所属部门id列表,不超过100个
        :return:
        '''
        create_member_url = f"{self.base_url}/user/create"
        params = {
            "userid": user_id,
            "name": name,
            "mobile": mobile,
            "department": department
        }
        r = self.send(1, create_member_url, json=params)
        return r.json()

    def get_member(self, userid):
        '''
        # 调用查询成员接口，GET请求
        :param user_id: 成员UserID。对应管理端的帐号，企业内必须唯一
        :return:
        '''
        get_member_url = f"{self.base_url}/user/get"
        params = {
            "userid": userid
        }
        r = self.send(0, get_member_url, params=params)
        return r.json()

    def update_member(self, user_id, name, mobile):
        '''
        # 调用更新成员接口，POST请求
        :param user_id:成员UserID。对应管理端的帐号，企业内必须唯一
        :param name:成员名称。
        :param mobile:手机号码。企业内必须唯一
        :return:
        '''
        update_member_url = f"{self.base_url}/user/update"
        params = {
            "userid": user_id,
            "name": name,
            "mobile": mobile
        }
        r = self.send(1, update_member_url, json=params)
        return r.json()

    def delete_member(self, userid):
        '''
        # 调用删除成员接口，GET请求
        :param user_id: 成员UserID。对应管理端的帐号，企业内必须唯一
        :return:
        '''
        delete_member_url = f"{self.base_url}/user/delete"
        params = {
            "userid": userid
        }
        r = self.send(0, delete_member_url, params=params)
        # r = self.s.get(delete_member_url, params=params)
        return r.json()
