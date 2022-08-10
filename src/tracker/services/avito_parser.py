import requests
from bs4 import BeautifulSoup


def get_number_of_ads(query: str, region: str) -> int:
    """
    Get number of ads on avito.ru by 'query' in 'region'
    """
    raw_content = _get_page_content(query, region)
    page = BeautifulSoup(raw_content, 'lxml')
    number = page.find(class_='page-title-count-wQ7pG').text
    return _get_int(number)


def _get_page_content(query: str, region: str) -> bytes:
    """
    Send request to avito.ru using 'query' and 'region' and returns page content
    """
    url = f"https://www.avito.ru/{region}?q={query}"
    query = requests.get(url)
    content = query.content
    return content


def _get_int(string: str) -> int:
    """
    Parse decimal numbers from string and convert it to integer number.

    Necessary because the raw string from avito.ru contains symbols with ASCII code == 160,
    and the 'int()' function can't convert it to an integer number.
    """
    result = ''
    for c in string:
        if '0' <= c <= '9':
            result += c
    return int(result)
