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
* [Interface](#chapter-1)
* [Getting started](#chapter-2)
* [Source code](#chapter-3)
* [License](#chapter-5)

<a id="chapter-0"></a>

## :page_facing_up: Project description

A service that allows you to monitor changes in the number of ads in Avito for a specific search query and region.

**[Technical specification (RU)](./docs/technical_specification_ru.md)**

<a id="chapter-1"></a>

## :camera: Interface

<a id="chapter-2"></a>

## :hammer: Getting started

1. Download this repository
    * Option 1
        1. Install [git](https://git-scm.com/download)
        2. Clone this repository
        ```bash
        git clone https://github.com/Yu-Leo/avito-tracker.git
        cd avito-tracker
        ```
    * Option 2 - [Download ZIP](https://github.com/Yu-Leo/avito-tracker/archive/refs/heads/main.zip)
2. Create `.env` file and set the values of the [required environment variables](#envvars)
3. Run application using Docker compose
    ```bash
    docker-compose up --build
    ```

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
- **Docker** and **Docker compose**

### :wrench: Settings

<a id="envvars"></a>

#### Required environment variables:

- Settings for DBMS (PostgreSQL):
    - `POSTGRES_DB`
    - `POSTGRES_USER`
    - `POSTGRES_PASSWORD`

### :mag: Logging

Logs saving to the `./logs.log` file.

**Example:**

```
2022-08-12T11:04:32.491389+0300 ERROR (psycopg2.OperationalError) connection to server at "localhost" (127.0.0.1), port 5432 failed: Connection refused
	Is the server running on that host and accepting TCP/IP connections?

(Background on this error at: https://sqlalche.me/e/14/e3q8)
2022-08-12T11:04:32.491789+0300 ERROR Error in working with the database
```

<a id="chapter-5"></a>

## :open_hands: License

Author: [Yu-Leo](https://github.com/Yu-Leo)

License: [GNU General Public License v3.0](./LICENSE)

If you use my code, please put a star ⭐️ on the repository.
