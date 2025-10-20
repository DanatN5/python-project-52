### Hexlet tests and linter status:
[![Actions Status](https://github.com/DanatN5/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/DanatN5/python-project-52/actions)



## Менеджер задач

> Веб-приложение для анализа SEO-параметров сайтов
> Позволяет сохранять URL-адреса, выполнять проверки и собирать информацию о заголовках и метаданных

# Демонстрация проекта
Приложение доступно по ссылке: [Открыть сайт](https://python-project-52-rutz.onrender.com/)


## Установка и запуск:
# Клонировать репозиторий
``` 
git clone git@github.com:DanatN5/python-project-52.git
```
````
cd python-project-52
````

# Сконфигурируйте файл .env с со следущими переменными:

SECRET_KEY
DEBUG
DATABASE_URL
ALLOWED_HOSTS
ROLLBAR_TOKEN

# Установка зависимостей и создание таблиц в базе данных
`````
make build
``````

# Запуск приложения
````````
make start
````````