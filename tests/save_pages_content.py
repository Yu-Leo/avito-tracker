from typing import Optional

import requests


def get_and_save_page_content(query: str, region: str, filename: Optional[str] = None):
    if not filename:
        filename = f'{query}_{region}.txt'
    url = f'https://www.avito.ru/{region}?q={query}'
    request = requests.get(url)
    content = request.content
    with open(f'pages_content/{filename}', 'wb') as file:
        file.write(content)


def main(correct_avito_queries: Optional[list[tuple[str, str]]] = None,
         incorrect_avito_queries: Optional[list[tuple[str, str]]] = None) -> None:
    if correct_avito_queries is None:
        correct_avito_queries = []
    if incorrect_avito_queries is None:
        incorrect_avito_queries = []

    for avito_query in correct_avito_queries:
        get_and_save_page_content(*avito_query)
    for i in range(len(incorrect_avito_queries)):
        get_and_save_page_content(*incorrect_avito_queries[i], filename=f'incorrect_query_{i}.txt')


if __name__ == '__main__':
    main([('book', 'moskva'), ('laptop', 'moskva'), ],
         [('123', '123')])
