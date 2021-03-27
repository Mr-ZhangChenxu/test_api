# /usr/local/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021-03-27  11:15 上午
# @Author  : 张晨旭
# @IDE     : PyCharm
# @PROJECT : Test_Api
# @File    : test_address.py
import pytest
import yaml

from test_conntact.contact_api.address_api import AddressApi


class TestAddress():
    '''
    编写测试用例，并进行相应的数据清洗
    '''
    def setup(self):
        '''
        实例化AddressApi()
        :return:
        '''
        self.address = AddressApi()

    @pytest.mark.parametrize(("user_id", "name", "mobile", "department"),
                             yaml.safe_load(open("../datas/members.yml","r",encoding="utf-8"))["create_member"])
    def test_create_member(self, user_id, name, mobile, department):
        # 创建前后都执行删除操作，进行数据清理
        self.address.delete_member(user_id)
        try:
            r = self.address.create_member(user_id, name, mobile, department)
        finally:
            self.address.delete_member(user_id)
        assert r.get('errmsg') == 'created'

    @pytest.mark.parametrize(("user_id", "name", "mobile", "department"),
                             yaml.safe_load(open("../datas/members.yml", "r", encoding="utf-8"))["get_member"])
    def test_get_member(self, user_id, name, mobile, department):
        # 查询前创建成员，查询后删除成员
        self.address.create_member(user_id, name, mobile, department)
        try:
            r = self.address.get_member(user_id)
        finally:
            self.address.delete_member(user_id)
        pytest.assume(r.get('errmsg') == 'ok')
        pytest.assume(r.get('name') == name)

    @pytest.mark.parametrize(("user_id", "name", "mobile", "department"),
                             yaml.safe_load(open("../datas/members.yml", "r", encoding="utf-8"))["update_member"])
    def test_update_member(self, user_id, name, mobile, department):
        # 更新成员之前保证是新创建成员，更新之后删除
        self.address.create_member(user_id, name, mobile, department)
        try:
            new_name = name+'a'
            r = self.address.update_member(user_id, new_name, mobile)
        finally:
            self.address.delete_member(user_id)
        pytest.assume(r.get('errmsg') == 'updated')
        pytest.assume(r.get('errcode') == 0)

    @pytest.mark.parametrize(("user_id", "name", "mobile", "department"),
                             yaml.safe_load(open("../datas/members.yml", "r", encoding="utf-8"))["delete_member"])
    def test_delete_member(self, user_id, name, mobile, department):
        # 删除之前先创建成员
        self.address.create_member(user_id, name, mobile, department)
        r = self.address.delete_member(user_id)
        pytest.assume(r.get("errmsg") == "deleted")
        r = self.address.get_member(user_id)
        pytest.assume(r.get("errcode") == 60111)

