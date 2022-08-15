"""
Main application file
"""
import threading

import uvicorn
from loguru import logger

from tracker.db import Session
from tracker.services.periodic_parser import periodic_parser
from tracker.settings import settings

if __name__ == "__main__":
    logger.add('../../logs.log',
               format='{time} {level} {message}',
               level='ERROR')

    periodic_parser_thread = threading.Thread(target=periodic_parser,
                                              args=(Session, settings.REQUESTS_PERIOD,),
                                              name='periodic_parser_thread',
                                              daemon=True)
    periodic_parser_thread.start()
    uvicorn.run('app:app',
                host=settings.SERVER_HOST,
                port=settings.SERVER_PORT,
                reload=True)
