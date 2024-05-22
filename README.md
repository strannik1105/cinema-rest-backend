# cinema-rest-backend

## стэк

    Python 3.12  
    FastApi - веб фреймфорк
    SQLAlchemy - ORM
    Postgres - СУБД

## запуск

файл docker-compose.yaml содержит в себе сервисы котоые необходимо поднять для работы проекта:

* PostgreSQL
* Бэкенд

Для запуска необходимо выполнить команду:

    docker-compose up --build -d

Сервисы будут подняты и запущены в фоне