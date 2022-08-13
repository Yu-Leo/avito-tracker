import pytest

from tracker import models


@pytest.mark.parametrize('data', [{'query': 'book',
                                   'region': 'moskva'}])
def test_add(data, client, session):
    # Act
    response = client.post('/add', json=data)

    # Assert
    assert response.status_code == 200
    object_from_db = session.query(models.AvitoQuery).first()
    assert object_from_db.query == data['query'] and object_from_db.region == data['region']
