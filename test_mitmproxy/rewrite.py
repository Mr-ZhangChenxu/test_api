# /usr/local/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021-03-20  上午10:43
# @Author  : 张晨旭
# @IDE     : PyCharm
# @File    : rewrite.py
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
            # 修改原始数据
            # 获取的text 是str类型，如果要对数据进行操作，需要进行数据转换
            data = json.loads(flow.response.text)
            data['data']['items'][1]['quote']['name'] = '中国平安'*2
            data['data']['items'][2]['quote']['name'] = ' '
            # 赋值给响应信息
            flow.response.text = json.dumps(data)


addons = [
    Counter()
]