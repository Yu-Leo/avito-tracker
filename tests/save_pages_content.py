import requests


def get_and_save_page_content(query: str, region: str):
    url = f'https://www.avito.ru/{region}?q={query}'
    request = requests.get(url)
    content = request.content
    with open(f'pages_content/{query}_{region}.txt', 'wb') as file:
        file.write(content)


def main(avito_queries: list[tuple[str, str]]):
    for avito_query in avito_queries:
        get_and_save_page_content(*avito_query)


if __name__ == '__main__':
    main([('book', 'moskva'),
          ('laptop', 'moskva'), ])
