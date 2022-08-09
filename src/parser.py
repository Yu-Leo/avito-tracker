import requests
from bs4 import BeautifulSoup


def _get_int(number: str) -> int:
    result = ''
    for n in number:
        if '0' <= n <= '9':
            result += n
    return int(result)


def get_number_of_ads(query: str, region: str) -> int:
    url = f"https://www.avito.ru/{region}?q={query}"
    q = requests.get(url)
    content = q.content
    soup = BeautifulSoup(content, 'lxml')
    number = soup.find(class_='page-title-count-wQ7pG').text
    return _get_int(number)


if __name__ == '__main__':
    print(get_number_of_ads('book', 'moskva'))
