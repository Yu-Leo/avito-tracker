"""
File with functions for periodically receiving information from avito.ru and saving it
"""
import datetime
import time

from loguru import logger

from tracker.exceptions import ParserError, DatabaseError
from tracker.schemas import AvitoQueryValueCreate
from tracker.services.avito_parser import get_number_of_ads
from tracker.services.avito_queries import AvitoQueryService, AvitoQueryValueService


def _parse_and_save_data(session) -> None:
    avito_query_service = AvitoQueryService(session)
    avito_query_value_service = AvitoQueryValueService(session)

    avito_queries = avito_query_service.get_list()
    for avito_query in avito_queries:
        avito_query_value = AvitoQueryValueCreate(
            avito_query_id=avito_query.id,
            timestamp=datetime.datetime.now(),
            value=get_number_of_ads(query=avito_query.query, region=avito_query.region)
        )
        avito_query_value_service.create(avito_query_value)


def periodic_parser(Session, requests_period: int) -> None:
    while True:
        start_time = time.time()
        try:
            session = Session()
            _parse_and_save_data(session)
            session.close()
        except (ParserError, DatabaseError) as e:
            logger.error(e)
        finish_time = time.time()
        requests_execution_time = finish_time - start_time
        time.sleep(requests_period - requests_execution_time)
