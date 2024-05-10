#!/usr/bin/env python
# encoding: utf-8
'''
@author: LoRexxar
@contact: lorexxar@gmail.com
@file: BaseScan.py
@time: 2023/5/10 18:48
@desc:

'''


from utils.LReq import LReq
from urllib.parse import urlparse


class BaseSimc:
    def __init__(self):
        self.crit_rate = 0.05
        self.haste = 1
        self.mastery = 0
        self.versatility = 1

        self.target_count = 1
        self.simc_time = 300

        # 最小buff计算间隔
        self.base_timecheck_min = 0.1
        # 当前buff列表
        self.active_self_buff_list = []
        # 敌方buff列表
        self.active_enemy_buff_list = []
        for i in range(self.target_count):
            self.active_enemy_buff_list.append([])
        # 基础技能列表
        self.base_skill_list = []
        # 当前技能优先级列表
        self.skill_priority_list = []

        self.total_damage = 0

        self.init_status()
        self.init_simc()
        self.init_skill_list()
        self.load_skill_priority_list()

    def init_status(self):
        self.crit_rate = 0.30  # 暴击率
        self.haste = 1.30  # 急速
        self.mastery = 1.50  # 精通
        self.versatility = 1.20  # 全能

    def init_simc(self):
        self.target_count = 5
        self.simc_time = 40

    def init_skill_list(self):
        self.base_skill_list = []

    def load_skill_priority_list(self):
        self.skill_priority_list = []

    def base_simc(self):
        # base simc
        return self.total_damage
