import os

import pytest
import requests_mock

from tracker.exceptions import AvitoQueryError
from tracker.services.avito_parser import get_number_of_ads

PAGES_CONTENT_DIR = 'tests/pages_content'  # Path to folder with pages content for tests


@pytest.mark.skip(reason="too long...")
class TestWithRealService:
    def test_get_number_of_ads_with_correct_values(self):
        result = get_number_of_ads('book', 'moskva')
        assert isinstance(result, int)
        assert result > 0

    def test_get_number_of_ads_with_incorrect_values(self):
        with pytest.raises(AvitoQueryError):
            get_number_of_ads('book', '123')


def get_test_queries_from_dir():
    test_files = [item for item in os.listdir(PAGES_CONTENT_DIR) if
                  os.path.isfile(os.path.join(PAGES_CONTENT_DIR, item))]
    result = []
    for filename in test_files:
        if filename.count('_') == 1:
            result.append((filename[:filename.find('_')], filename[filename.find('_') + 1:filename.rfind('.')]))
    return result


class TestWithMockedService:
    @pytest.mark.parametrize('query, region', get_test_queries_from_dir())
    def test_get_number_of_ads_with_correct_values(self, query, region):
        with open(f'tests/pages_content/{query}_{region}.txt', 'rb') as file:
            page_content = file.read()
        with requests_mock.Mocker() as mock:
            mock.get(f'https://www.avito.ru/{region}?q={query}', content=page_content)
            result = get_number_of_ads(query, region)
            assert isinstance(result, int)
            assert result > 0

    @pytest.mark.parametrize('query, region', [('123', '123')])
    def test_get_number_of_ads_with_incorrect_values(self, query, region):
        with open(f'tests/pages_content/incorrect_query_0.txt', 'rb') as file:
            page_content = file.read()
        with requests_mock.Mocker() as mock:
            mock.get(f'https://www.avito.ru/{region}?q={query}', content=page_content)
            with pytest.raises(AvitoQueryError):
                get_number_of_ads(query, region)
