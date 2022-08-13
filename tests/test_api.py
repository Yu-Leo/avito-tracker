import pytest


@pytest.mark.parametrize('data', [{'query': 'book',
                                   'region': 'moskva'}])
def test_add(data, client):
    response = client.post('/add', json=data)
    assert response.status_code == 200
