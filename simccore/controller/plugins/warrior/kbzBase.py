#!/usr/bin/env python
# encoding: utf-8
'''
@author: LoRexxar
@contact: lorexxar@gmail.com
@file: lhfszsMonitor.py
@time: 2024/2/22 16:30
@desc:

'''

from datetime import datetime
from utils.log import logger
from simccore.controller.BaseSimc import BaseSimc
from simccore.webhook.aibotkWechat import AibotkWechatWebhook


class kbzBase(BaseSimc):
    """
    kbz
    """
    def __init__(self):
        super().__init__()

    def base_simc(self):
        pass



