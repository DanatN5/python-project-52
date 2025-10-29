### Hexlet tests and linter status:
[![Actions Status](https://github.com/DanatN5/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/DanatN5/python-project-52/actions)

[![Python CI](https://github.com/DanatN5/python-project-52/actions/workflows/build.yml/badge.svg)](https://github.com/DanatN5/python-project-52/actions/workflows/build.yml)

[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=DanatN5_python-project-52&metric=coverage)](https://sonarcloud.io/summary/new_code?id=DanatN5_python-project-52)



# Менеджер задач

> Веб-приложение предоставляющее ToDo-лист
> Позволяет создавать задачи, устанавлиать для них статус, назначать исполнителейЮ ставить метки

## Демонстрация проекта
Приложение доступно по ссылке: [Открыть сайт](https://python-project-52-rutz.onrender.com/)


## Установка и запуск:
### Клонировать репозиторий
``` 
git clone git@github.com:DanatN5/python-project-52.git
```
````
cd python-project-52
````

### Сконфигурируйте файл .env с со следущими переменными:

SECRET_KEY
DEBUG
DATABASE_URL
ALLOWED_HOSTS
ROLLBAR_TOKEN

## Установка зависимостей и создание таблиц в базе данных
`````
make build
``````

# Запуск приложения
````````
make start
````````