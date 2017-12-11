# _author_='shaojie'
# -*- coding:utf-8 -*-

import logging


class Log(object):

    def log(self,level,msg):

        logger = logging.getLogger('client')
        logger.setLevel(logging.DEBUG)

        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        formatter = logging.Formatter("'%(asctime)s - %(name)s - %(levelname)s - %(message)s'")
        ch.setFormatter(formatter)

        logger.addHandler(ch)
        if level == "debug":
            logger.debug(msg)
        elif level == "info":
            logger.info(msg)
        elif level == "error":
            logger.error(msg)
        elif level == "warning":
            logger.warning(msg)

        logger.removeFilter(ch)

    def info(self, msg):
        self.log('info',msg)

    def error(self, msg):
        self.log('error',msg)

    def warn(self, msg):
        self.log('warning', msg)

    def debug(self, msg):
        self.log('debug', msg)