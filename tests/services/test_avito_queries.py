import datetime

import pytest

from tracker import models
from tracker.schemas import AvitoQueryCreate, AvitoQueryValueCreate
from tracker.services.avito_queries import AvitoQueryService, AvitoQueryValueService


class TestAvitoQueryService:

    def test_create(self, session):
        # Arrange
        avito_query_service = AvitoQueryService(session)
        avito_query_data = AvitoQueryCreate(query='query',
                                            region='region')
        # Act
        created_object = avito_query_service.create(avito_query_data)

        # Assert
        object_from_db = session.query(models.AvitoQuery).get(created_object.id)
        assert created_object == object_from_db

    def test_get_list(self, session, avito_queries_list):
        # Arrange
        avito_query_service = AvitoQueryService(session)

        # Act
        list_from_db = avito_query_service.get_list()

        # Assert
        for i in range(10):
            assert (list_from_db[i].query == avito_queries_list[i].query and
                    list_from_db[i].region == avito_queries_list[i].region)


class TestAvitoQueryValueService:

    def test_create(self, session):
        # Arrange
        avito_query_value_service = AvitoQueryValueService(session)
        avito_query_value_data = AvitoQueryValueCreate(avito_query_id=1,
                                                       timestamp=datetime.datetime(2022, 8, 13, 10, 0, 0, 0),
                                                       value=0)
        # Act
        created_object = avito_query_value_service.create(avito_query_value_data)

        # Assert
        object_from_db = session.query(models.AvitoQueryValue).get(created_object.id)
        assert created_object == object_from_db

    @pytest.mark.parametrize('avito_query_id, start, end', [(1, None, None),
                                                            (1, '2022-08-13 00:00:00', None),
                                                            (1, '2022-08-12 00:00:00', '2022-08-14 00:00:00'),
                                                            (2, None, None), ])
    def test_get_by_avito_query_id(self, avito_query_id, start, end, session, avito_query_values_list):
        # Arrange
        avito_query_value_service = AvitoQueryValueService(session)

        # Act
        list_from_db = avito_query_value_service.get_by_avito_query_id(avito_query_id, start, end)

        # Assert
        for item in list_from_db:
            assert item.avito_query_id == avito_query_id
            if start is not None:
                assert start <= str(item.timestamp)
            if end is not None:
                assert str(item.timestamp) <= end
