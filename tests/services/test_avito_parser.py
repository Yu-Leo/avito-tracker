import pytest

from tracker.exceptions import AvitoQueryError
from tracker.services.avito_parser import get_number_of_ads


@pytest.mark.parametrize('query, region', [('book', 'moskva'),
                                           ('laptop', 'moskva'),
                                           ])
def test_get_number_of_ads_with_correct_values(query, region):
    result = get_number_of_ads(query, region)
    assert isinstance(result, int)
    assert result > 0


def test_get_number_of_ads_with_incorrect_values():
    with pytest.raises(AvitoQueryError):
        result = get_number_of_ads('book', '123')
