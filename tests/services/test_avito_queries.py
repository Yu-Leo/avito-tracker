from tracker.schemas import AvitoQueryCreate
from tracker.services.avito_queries import AvitoQueryService


def test_create_avito_query(database_session):
    avito_query_service = AvitoQueryService(database_session)
    avito_query_data = AvitoQueryCreate(query='query',
                                        region='region')

    created_object = avito_query_service.create(avito_query_data)

    object_from_db = avito_query_service.get_list()[0]
    assert created_object == object_from_db
