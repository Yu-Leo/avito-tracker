import datetime
import functools
import time

from tracker.db import Session
from tracker.schemas import AvitoQueryValueCreate
from .avito_parser import get_number_of_ads
from .avito_queries import AvitoQueryService, AvitoQueryValueService


def create_session(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        session = Session()
        func(session, *args, **kwargs)
        session.close()

    return inner


@create_session
def _parse_and_save_data(session: Session):
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


def periodic_parser(requests_period: int):
    while True:
        start_time = time.time()
        _parse_and_save_data()
        finish_time = time.time()
        requests_execution_time = finish_time - start_time
        time.sleep(requests_period - requests_execution_time)
