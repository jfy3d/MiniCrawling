from app.common.func import bytes_to_str
import settings
import time
import json
import multiprocessing
import traceback
from multiprocessing import cpu_count
from app.loader.site_loader import SiteLoader
import logging

logger = logging.getLogger('crawler')

CLASS_MAP = []
PACKAGE_MAP = {}


def get_spider(classname):
    _class = classname.replace('#', '').split('?')[0]
    _path = _class.split('.')
    _module = '.'.join(_path[:-1])
    _module = '%s' % _module
    _name = _path[-1]
    if not CLASS_MAP.__contains__(_class):
        PACKAGE_MAP[_module] = __import__(_module, {}, {}, _name)
        CLASS_MAP.append(_class)
    return getattr(PACKAGE_MAP[_module], _name)


class Crawler:
    def start(self):
        crawler_list = SiteLoader().getWebsiteList()
        for config in crawler_list:

            try:
                _crawler_class = get_spider(config['crawler'])
                _crawler = _crawler_class(config)
                logger.info('crawler process !')
                _crawler.process()
            except KeyboardInterrupt as e:
                logger.warning("KeyboardInterrupt 中断进程 ")
                break
            except:
                logger.error(traceback.print_exc())


def start_crawler():
    crawler = Crawler()
    crawler.start()

