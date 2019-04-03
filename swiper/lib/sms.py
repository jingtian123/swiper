"""发短信功能"""
import random

import requests
from django.core.cache import cache

from common import keys
from swiper import config


def gen_vcode(length=4):
    # 生成1000 - 9999 的随机验证码
    start = 10 ** (length - 1)
    end = 10 ** length-1
    return random.randint(start, end)


def send_sms(phonenum):
    vcode = gen_vcode()
    # 把验证码加入缓存,缓存180秒
    cache.set(keys.VCODE_KEY % phonenum, str(vcode), 300)
    url = config.YZX_SMS_API
    params = config.YZX_SMS_PARAMS.copy()
    params['param'] = vcode
    params['mobile'] = phonenum
    resp = requests.post(url, json=params)

    # 对结果做一些检查
    if resp.status_code == 200:
        result = resp.json()
        if result['code'] == '000000':
            return True, result['msg']
        else:
            return False, result['msg']
    else:
        return '短信服务器通信错误!'




