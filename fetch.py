import time
import logging

from bookshelf.parser import Parser

logger = logging.getLogger(__name__)


def periodic_fetch():
    while True:
        logger.info("Fetching XML file")
        try:
            Parser.fetch()
        except Exception as e:
            logger.error(e)

        time.sleep(3600)
