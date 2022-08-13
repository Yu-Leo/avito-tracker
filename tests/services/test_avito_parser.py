import pytest
import requests_mock

from tracker.exceptions import AvitoQueryError
from tracker.services.avito_parser import get_number_of_ads


@pytest.mark.skip(reason="too long...")
class TestWithRealService:
    def test_get_number_of_ads_with_correct_values(self):
        result = get_number_of_ads('book', 'moskva')
        assert isinstance(result, int)
        assert result > 0

    def test_get_number_of_ads_with_incorrect_values(self):
        with pytest.raises(AvitoQueryError):
            result = get_number_of_ads('book', '123')


class TestWithMockedService:

    @pytest.mark.parametrize('query, region', [('book', 'moskva')])
    def test_get_number_of_ads_with_correct_values(self, query, region):
        with open(f'tests/pages_content/{query}_{region}.txt', 'rb') as file:
            page_content = file.read()
        with requests_mock.Mocker() as mock:
            mock.get(f'https://www.avito.ru/{region}?q={query}', content=page_content)
            result = get_number_of_ads('book', 'moskva')
            assert isinstance(result, int)
            assert result > 0
