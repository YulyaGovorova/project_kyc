# KYC
Дипломный проект курса.
DRF сервис по обработке загружаемых данных администратором(API для приема документов со стороны фронтенда).


### Для работы с проектом необходимо выполнить следующие действия:
- Клонировать репозиторий.
- Заполнить файл .env своими данными (на примере файла .env.sample)
- Установить зависимости pip install -r requirements.txt
- Создать базу данных в PostreSQL CREATE DATABASE django_rest;
- Создать python manage.py makemigration и применить миграции python manage.py migrate
- Создать пользователя командой python manage.py csu
- Установить и запустить Docker Desktop локально
- Собрать образ и запустить контейнеры командой docker-compose up --build
- Откройте браузер и перейдите по адресу http://127.0.0.1:8000 для доступа к приложению.
- Документация API:

http://127.0.0.1:8000/docs/ - Swagger

http://127.0.0.1:8000/redoc/ - Redoc

## Требуемый стэк

- python
- postgresql
- docker
- Django + DRF