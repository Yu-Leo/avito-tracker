<h1 align="center"> Avito tracker </h1>

<p align="center">
  <a href="https://github.com/Yu-Leo/avito-tracker/blob/main/LICENSE" target="_blank"> <img alt="license" src="https://img.shields.io/github/license/Yu-Leo/avito-tracker?style=for-the-badge&labelColor=090909"></a>
  <a href="https://github.com/Yu-Leo/avito-tracker/releases/latest" target="_blank"> <img alt="last release" src="https://img.shields.io/github/v/release/Yu-Leo/avito-tracker?style=for-the-badge&labelColor=090909"></a>
  <a href="https://github.com/Yu-Leo/avito-tracker/commits/main" target="_blank"> <img alt="last commit" src="https://img.shields.io/github/last-commit/Yu-Leo/avito-tracker?style=for-the-badge&labelColor=090909"></a>
  <a href="https://github.com/Yu-Leo/avito-tracker/graphs/contributors" target="_blank"> <img alt="commit activity" src="https://img.shields.io/github/commit-activity/m/Yu-Leo/avito-tracker?style=for-the-badge&labelColor=090909"></a>
</p>

<hr>

## Navigation

* [Project description](#chapter-0)
* [API](#chapter-1)
* [Getting started](#chapter-2)
* [Source code](#chapter-3)
* [License](#chapter-5)

<a id="chapter-0"></a>

## :page_facing_up: Project description

A service that allows you to monitor changes in the number of ads in Avito for a specific search query and region.

**[Technical specification (RU)](./docs/technical_specification_ru.md)**

<a id="chapter-1"></a>

## :pushpin: API

- **POST** `/add` - accepts a search phrase and a region, registers them in the system. Returns the id of this pair.

  _Example:_

    - Send:
      ```json
      {
      "query": "book",
      "region": "moskva"
      }
      ```

    - Get:
      ```json
      {
      "id": 8
      }
      ```

- **GET** `/stat` - accepts as input the id of the bundle search phrase + region and the interval for which you want to
  output counters. Returns counters and their corresponding timestamps.

  _Example:_

    - Send: GET `http://127.0.0.1:8000/stat?avito_query_id=6&start=2022-08-12T00:00:00&end=2022-08-15T00:00:00`

    - Get:
      ```json
      [{
      "timestamp": "2022-08-12T11:05:00",
      "value": "1257"
      },
      {
      "timestamp": "2022-08-12T11:05:10",
      "value": "1257"
      },
      {
      "timestamp": "2022-08-12T11:05:20",
      "value": "1257"
      },
      {
      "timestamp": "2022-08-13T15:02:43",
      "value": "1264"
      }]
      ```

<a id="chapter-2"></a>

## :hammer: Getting started - [tutorial](./docs/getting_started.md)

<a id="chapter-3"></a>

## :computer: Source code

### :books: [Technical documentation](./docs/README.md)

### :wrench: Technologies

- DBMS: **PostgreSQL**
- Programming language: **Python (3.10.4)**
- Frameworks and libraries:
    - **FastAPI**
    - **SQLAlchemy**
    - **Alembic**
    - **Loguru**

### :mag: Logging

Logs saving to the `./logs.log` file.

**Example:**

```
2022-08-12T11:04:32.491389+0300 ERROR (psycopg2.OperationalError) connection to server at "localhost" (127.0.0.1), port 5432 failed: Connection refused
	Is the server running on that host and accepting TCP/IP connections?

(Background on this error at: https://sqlalche.me/e/14/e3q8)
2022-08-12T11:04:32.491789+0300 ERROR Error in working with the database
```

### :coffee: Tests ![coverate](https://img.shields.io/badge/coverage-81%25-green)

Run all tests:

```bash
pytest tests/
```

With `coverage`:

```bash
pytest tests/ --cov=src/tracker 
```

With report page generation:

```bash
pytest tests/ --cov=src/tracker --cov-report=html 
```

<a id="chapter-5"></a>

## :open_hands: License

Author: [Yu-Leo](https://github.com/Yu-Leo)

License: [GNU General Public License v3.0](./LICENSE)

If you use my code, please put a star ⭐️ on the repository.
