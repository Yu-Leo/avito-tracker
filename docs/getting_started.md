# Getting started

1. Download this repository
   * Option 1
      1. Install [git](https://git-scm.com/download)
      2. Clone this repository
       ```bash
       git clone https://github.com/Yu-Leo/avito-tracker.git
       cd avito-tracker
       ```
   * Option 2 - [Download ZIP](https://github.com/Yu-Leo/avito-tracker/archive/refs/heads/main.zip)
3. Create `.env` file and add your configurations in it
   - Settings for PostgreSQL:
      - `POSTGRES_DB`
      - `POSTGRES_USER`
      - `POSTGRES_PASSWORD`
   - Settings for application:
      - `DB_HOST` (default `localhost`)
      - `DB_PORT` (default `5432`)
      - `DB_USER`
      - `DB_PASSWORD`
      - `DB_NAME`
4. Create a virtual environment in the project repository
    ```bash
    python3 -m venv venv
    ```
5. Activate the virtual environment
    ```bash
    source venv/bin/activate
    ```
6. Install project dependencies
   ```bash
    pip install -r requirements.txt
    ```
7. Run PostgreSQL in docker container using docker compose
    ```bash
    docker-compose up
    ```   
8. Run application
    ```bash
    python3 src/tracker/main.py
    ```

## :arrow_left: [Back to README](../README.md)
