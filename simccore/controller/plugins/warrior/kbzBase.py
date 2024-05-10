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

from kbz.skill import SKILL_Dict


class kbzBase(BaseSimc):
    """
    kbz
    """
    def __init__(self):
        super().__init__()

        self.base_skill_list = list(SKILL_Dict.keys())
        self.init_skill_list()

    def init_skill_list(self):
        for base_skill in self.base_skill_list:
            self.skill_active_CD[base_skill] = {
                "activeCD": 0,
                "charge": SKILL_Dict[base_skill]["charge"]
            }

    def base_simc(self):
        # 初始化基础向量
        active_time = 0





