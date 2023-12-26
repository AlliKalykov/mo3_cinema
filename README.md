    Для создания django-проекта необходимо выполнить следующие команды:
1. Создать виртуальное окружение:
    ```
    python -m venv venv
    ```
2. Активировать виртуальное окружение:
    ```
    source venv/bin/activate
    ```
3. Установить зависимости:
    ```
    pip install django
    ```
4. Проинициализировать гит-репозиторий:
    ```
    git init
    ```
5. Создать файл .gitignore и добавить в него следующие строки:
    ```
    - файлы кеширования
    - настройки IDE
    - виртуальное окружение
    - environment variables
6. Создать файл requirements.txt и заполнить его зависимостями:
    ```
    pip freeze > requirements.txt
    ```
7. Создать django-проект:
    ```
    django-admin startproject cinema
    ```
8. Запустить проект и проверить работоспособность (находясь в папке cinema или же указав полный путь к manage.py):
    ```
    python manage.py runserver
    ```
9. Сделать миграцию:
    ```
    python manage.py migrate
    ```
10. Создать суперпользователя:
    ```
    python manage.py createsuperuser
    ```
11. Создать приложение:
    ```
    python manage.py startapp movies
    ```
12. Зарегистрировать приложение в settings.py:
    ```
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        'movies.apps.MoviesConfig',
    ]
    ```