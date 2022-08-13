import pytest
from fastapi import status

from tracker import models


@pytest.mark.parametrize('data', [{'query': 'book',
                                   'region': 'moskva'}])
def test_add(data, client, session):
    # Act
    response = client.post('/add', json=data)

    # Assert
    assert response.status_code == status.HTTP_200_OK
    object_from_db = session.query(models.AvitoQuery).first()
    assert object_from_db.query == data['query'] and object_from_db.region == data['region']


stat_test_data = [({'avito_query_id': 1},
                   [{'timestamp': '2022-08-13T00:00:00', 'value': '1'},
                    {'timestamp': '2020-08-13T00:00:00', 'value': '1'},
                    {'timestamp': '2023-08-13T00:00:00', 'value': '1'}]),

                  ({'avito_query_id': 1, 'start': '2022-08-12T00:00:00'},
                   [{'timestamp': '2022-08-13T00:00:00', 'value': '1'},
                    {'timestamp': '2023-08-13T00:00:00', 'value': '1'}]),

                  ({'avito_query_id': 1, 'start': '2022-08-12T00:00:00', 'end': '2022-08-14T00:00:00'},
                   [{'timestamp': '2022-08-13T00:00:00', 'value': '1'}])]


@pytest.mark.parametrize('data, result', stat_test_data)
def test_stat_with_correct_values(data, result, client, add_avito_query_values):
    # Act
    response = client.get('/stat', params=data)

    # Assert
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == result


def test_stat_with_incorrect_values(client, add_avito_query_values):
    # Act
    response = client.get('/stat', params={'avito_query_id': 1, 'start': 'asdf'})

    # Assert
    assert response.status_code == status.HTTP_400_BAD_REQUEST
