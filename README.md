# vidita test work by ewan

1 - Запустите в докере БД этой коммандой

-- docker run --name my_database -e POSTGRES_USER=ewan -e POSTGRES_PASSWORD=Dctjabutyyj100geljd -p 5432:5432 -d postgres

2 - Создайте миграции.

-- python manage.py makemigrations

-- python manage.py migrate

3 - Создайте суперпользователя.

Пользуйтесь...

Настроена админка - http://127.0.0.1:8000/admin/

Документация (Swagger) Open API - http://127.0.0.1:8000/swagger/

пример запроса в URL

http://127.0.0.1:8000/api/pictures_filter/?search=То_что_ищу
