# /usr/local/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021-03-20  下午12:21
# @Author  : 张晨旭
# @IDE     : PyCharm
# @File    : replace.py
import json
from mitmproxy import ctx, http


class Counter:

    name_list: list = ['腾讯控股','中国平安','中远海控']
    count = 0
    def __init__(self):
        self.num = 0

    def request(self, flow: http.HTTPFlow):
        self.num = self.num + 1
        ctx.log.info("We've seen %d flows" % self.num)

    def response(self, flow: http.HTTPFlow):
        # 通过url确定对应的接口信息
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t=" in flow.request.pretty_url:
            # 修改原始数据
            # 每次执行重置count为0
            self.count = 0
            # 获取的text 是str类型，如果要对数据进行操作，需要进行数据转换
            data = json.loads(flow.response.text)
            # 赋值给响应信息
            flow.response.text = json.dumps(self.json_travel(data))

    def json_travel(self, data):
        # 判断传入的数据类型{"a": {"b":{"c":1}}}
        if isinstance(data, dict):
            # 遍历字典的数据
            # 当字典格式，递归value值
            for key, value in data.items():
                data[key] = self.json_travel(value)
        elif isinstance(data, list):
            # 当数据类型 为 list 的时候， 添加到结构内，并继续递归遍历，
            # 直到数据类型不为可迭代对象时
            data = [self.json_travel(value) for value in data]
        # 第二个股票名字加长一倍 第三个股票名字置空
        elif isinstance(data, str):
            # 对name列表遍历修改：第二个股票名字加长一倍；第三个股票名字置空
            for name in self.name_list:
                if data == name:
                    self.count += 1
                    if self.count == 2:
                        data = data*2
                    elif self.count == 3:
                        data = ''
                    else:
                        data =data
        else:
            data = data
        return data

addons = [
    Counter()
]
