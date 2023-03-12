from app.loader.site_loader import SiteLoader
from app.common.log import setup_logger
from app.service import start_crawler
import settings
import logging


def start():
    setup_logger(settings.LOG_PATH, 'crawler', 'crawler.log', format='%(asctime)s %(filename)s %(lineno)d %(levelname)s %(message)s')
    logger = logging.getLogger('crawler')
    logger.info('start !')
    start_crawler()


# 启动服务
if __name__ == '__main__':
    start()

