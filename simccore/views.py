#!/usr/bin/env python
# encoding: utf-8


import time
import pytz
import datetime
import traceback
import threading
from utils.LReq import LReq
from utils.log import logger
from utils.threadingpool import ThreadPool

from simccore.models import MonitorTask
from LSimc.settings import THREAD_LIMIT_NUM

is_Block = False
lock = threading.Lock()


class LSimcCoreBackend:
    """
    monitor 守护线程
    """
    def __init__(self):
        pass

class LSimcCore:
    """
    主线程
    """

    def scan(self):

        try:
            pass
        except KeyboardInterrupt:
            logger.error("[Scan] Stop.")
            exit(0)

        except:
            logger.warning('[Scan] something error, {}'.format(traceback.format_exc()))
            raise