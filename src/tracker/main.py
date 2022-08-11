import os
import sys
import threading

import uvicorn
from loguru import logger

if __name__ == "__main__":
    sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

    from app import app
    from services.periodic_parser import periodic_parser
    from settings import settings

    logger.add('../../logs.log',
               format='{time} {level} {message}',
               level='ERROR')

    periodic_parser_thread = threading.Thread(target=periodic_parser,
                                              args=(settings.REQUESTS_PERIOD,),
                                              name='periodic_parser_thread',
                                              daemon=True)
    periodic_parser_thread.start()
    uvicorn.run(app,
                host=settings.SERVER_HOST,
                port=settings.SERVER_PORT, )
