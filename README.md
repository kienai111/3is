##  Система управления базой данных

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13+-blue.svg)
![Лицензия](https://img.shields.io/badge/Лицензия-MIT-green.svg)

Современное приложение для управления базой данных на Python и PostgreSQL с интуитивно понятным консольным интерфейсом.

##  Возможности

-  **Управление пользователями** - Добавление и просмотр пользователей
-  **Каталог товаров** - Управление товарами и ценами
-  **Интеграция с PostgreSQL** - Надежное подключение к базе данных
-  **Консольный интерфейс** - Простая в использовании система меню
-  **Конфигурация окружения** - Безопасное управление настройками

##  Быстрый старт

### Предварительные требования

- Python 3.8+
- PostgreSQL 13+
- pgAdmin 4

### Установка

1. **Клонируйте репозиторий**
   ```bash
   git clone https://github.com/kienai111/3is.git
   cd мой-проект-базы-данных

## Установите зависимости

1. **Откройте терминал в vs code**

pip install -r requirements.txt

2. **Настройка базы данных**

Создайте базу данных в pgAdmin 4 с именем my_prject_db

Обновите файл .env с вашими учетными данными

3. **Инициализация базы данных**

    **Откройте терминал в vs code**

python database.py

4. ## Запуск приложения

**Откройте терминал в vs code**

python app.py

5. ## Использование

**Откройте терминал в vs code**

 Приложение для управления базой данных
=====================================

1. Просмотреть пользователей
2. Добавить пользователя
3. Просмотреть товары
4. Добавить товар
5. Выход

Выберите опцию: 1
## Структура базы данных
Таблица пользователей
**SQL**

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
Таблица товаров
**SQL**
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2),
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

 ## Конфигурация

Создайте файл .env:

env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=my_database
DB_USER=postgres
DB_PASSWORD=ваш_пароль
APP_NAME=Система управления базой данных

## Разработка

**Структура проекта**

src/
├── app.py          # Основное приложение
├── database.py     # Операции с базой данных
├── config.py       # Настройки конфигурации
└── requirements.txt # Зависимости

**Запуск тестов**

**Откройте терминал в vs code**

python -m pytest tests/