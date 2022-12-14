# API YaTube

API на базе `Django REST framework` для проекта YaTube. Существует возможность публиковать записи, коментировать записи, подписываться и отписываться от авторов. А так же запрпашивать данные о уже существующих постах, групах и коментариях.
>
## Для установки проекта
>
### Установаите виртуальное окружение
``` python -m venv venv ``` / ``` python3 -m venv venv ```
>
### Активируйте виртуальное окружение
``` source venv/Scripts/activate ``` /  ``` . venv bin activate ```
>
### Установите requirements
``` pip install -r requirements.txt ```
>
### Выполните миграции
``` python manage.py migrate ```
>
## Примеры запросов
Get запрос на адрес `/api/v1/posts/` вернет список всех постов
>
Для добавления поста необходимо быть авторизированным и в запросе указать jwt токен, его можно получить по адресу `/api/v1/jwt/create/`
>
Пост можно добавить Post запросом на адрес `/api/v1/posts/`, обязательное поле в запросе - `text`, так же можно указать необязательные поля `group` - id группы в которой будет создан пост и `image` - строка закодированная в base64
>
