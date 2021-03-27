# /usr/local/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021-03-20  上午11:27
# @Author  : 张晨旭
# @IDE     : PyCharm
# @File    : map_local.py
import json
from mitmproxy import ctx, http


class Counter:
    def __init__(self):
        self.num = 0

    def request(self, flow: http.HTTPFlow):
        self.num = self.num + 1
        ctx.log.info("We've seen %d flows" % self.num)

    def response(self, flow: http.HTTPFlow):
        # 通过url确定对应的接口信息
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t=" in flow.request.pretty_url:
            # 加载本地的json文件
            with open('2.json', encoding='utf-8') as f:
                data = json.load(f)
            # 赋值给响应信息
            flow.response.text = json.dumps(data)

addons = [
    Counter()
]