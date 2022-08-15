import requests_mock

from tracker import models
from tracker.services.periodic_parser import _parse_and_save_data


def test__parse_and_save_data(session, add_real_avito_queries):
    # Arrange
    with open(f'tests/pages_content/book_moskva.txt', 'rb') as file:
        page_content = file.read()
    with requests_mock.Mocker() as mock:
        mock.get(f'https://www.avito.ru/moskva?q=book', content=page_content)

        # Act
        _parse_and_save_data(session)

    # Assert
    avito_query_values_from_db = session.query(models.AvitoQueryValue).filter_by(avito_query_id=1).all()
    assert len(avito_query_values_from_db) > 0
    assert isinstance(avito_query_values_from_db[0].value, int) and avito_query_values_from_db[0].value >= 0
