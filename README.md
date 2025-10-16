 Структура проекта:
 .env
 .gitignore
 app.py
 database.py
 requirements.txt

 # Система управления базой данных

[Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
[PostgreSQL](https://img.shields.io/badge/PostgreSQL-13+-blue.svg)


Современное приложение для управления базой данных на Python и PostgreSQL с интуитивно понятным консольным интерфейсом.

##  Возможности

-  **Управление пользователями** - Добавление и просмотр пользователей
-  **Каталог товаров** - Управление товарами и ценами
-  **Интеграция с PostgreSQL** - Надежное подключение к базе данных
-  **Консольный интерфейс** - Простая в использовании система меню
-  **Конфигурация окружения** - Безопасное управление настройками

## Быстрый старт

### Предварительные требования

- Python 3.8+
- PostgreSQL 13+
- pgAdmin 4

### Установка

1. **Клонируйте репозиторий**
   Terminal
   git clone https://github.com/kienai111/3is.git
   cd мой-проект-базы-данных    

2. **Установите зависимости**
    Terminal
    pip install -r requirements.txt

3. **Настройка базы данных**

Создайте базу данных в pgAdmin 4 с именем my_project_db

4. **Инициализация базы данных**
    Terminal
    python database.py

5. **Запуск приложения**
    Terminal
    python app.py

Использование приложения
Terminal
Приложение для управления базой данных
=====================================

1. Просмотреть пользователей
2. Добавить пользователя
3. Просмотреть товары
4. Добавить товар
5. Выход

Выберите опцию: 1

Структура базы данных

Таблица пользователей
sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
Таблица товаров
sql
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2),
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
