from flask import Response
import re
# 统一定义返回结果
def formatres(success=True,data={},msg=''):
    res = {
        "success":success,
        "data":data,
        "msg":msg
    }
    return res

# 允许跨域
def Response_headers(content):
    resp = Response(content)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp