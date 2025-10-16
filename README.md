Документация проекта "Система управления базой данных"
Оглавление
Введение

Архитектура системы

Установка и настройка

Конфигурация

Использование

API документация

Разработка

Устранение неисправностей

Часто задаваемые вопросы

Введение
Назначение системы
Система управления базой данных представляет собой консольное приложение на Python для управления пользователями и товарами в базе данных PostgreSQL. Система предназначена для демонстрации принципов работы с базами данных и может использоваться как основа для более сложных проектов.

Основные функции
Управление пользователями (добавление, просмотр)

Управление товарами (добавление, просмотр)

Статистика базы данных

Тестирование подключения к БД

Безопасное хранение конфигурации

Целевая аудитория
Разработчики, изучающие работу с PostgreSQL

Студенты курсов по базам данных

Разработчики, нуждающиеся в базовом шаблоне для работы с БД

Архитектура системы
Компоненты системы
text
Приложение (app.py)
        ↓
    DatabaseManager (database.py)
        ↓
    Конфигурация (config.py)
        ↓
    PostgreSQL База данных
Схема базы данных
sql
-- Таблица пользователей
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Таблица товаров
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2),
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
Взаимодействие компонентов
app.py - основной модуль приложения, отвечает за пользовательский интерфейс

database.py - слой работы с базой данных, содержит бизнес-логику

config.py - управление настройками приложения

PostgreSQL - система управления базами данных

Установка и настройка
Предварительные требования
Программное обеспечение
Python 3.8 или выше

PostgreSQL 13 или выше

pip (менеджер пакетов Python)

Системные требования
Оперативная память: 2 ГБ минимум

Свободное место на диске: 500 МБ

Операционная система: Windows 10+, Linux, macOS

Пошаговая установка
Шаг 1: Установка Python
bash
# Проверка установки Python
python --version
# или
python3 --version
Если Python не установлен, скачайте его с официального сайта: https://python.org

Шаг 2: Установка PostgreSQL
Windows:

Скачайте установщик с https://www.postgresql.org/download/windows/

Запомните пароль пользователя postgres

Linux (Ubuntu/Debian):

bash
sudo apt update
sudo apt install postgresql postgresql-contrib
macOS:

bash
brew install postgresql
brew services start postgresql
Шаг 3: Клонирование репозитория
bash
git clone https://github.com/ваш-username/мой-проект-базы-данных.git
cd мой-проект-базы-данных
Шаг 4: Установка зависимостей
bash
pip install -r requirements.txt
Шаг 5: Настройка базы данных
Запустите pgAdmin 4 или используйте командную строку

Создайте базу данных:

sql
CREATE DATABASE my_database;
Шаг 6: Настройка конфигурации
Создайте файл .env в корне проекта:

env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=my_database
DB_USER=postgres
DB_PASSWORD=ваш_пароль_от_postgres
APP_NAME=Система управления базой данных
Шаг 7: Инициализация базы данных
bash
python database.py
Шаг 8: Запуск приложения
bash
python app.py
Конфигурация
Файл .env
Файл .env содержит все чувствительные настройки приложения:

env
# Обязательные параметры
DB_HOST=localhost          # Хост базы данных
DB_PORT=5432              # Порт базы данных
DB_NAME=my_database       # Имя базы данных
DB_USER=postgres          # Имя пользователя БД
DB_PASSWORD=secret        # Пароль пользователя БД

# Дополнительные параметры
APP_NAME=Система управления БД  # Название приложения
DEBUG=False               # Режим отладки
Параметры подключения к БД
Параметр	Значение по умолчанию	Описание
DB_HOST	localhost	Адрес сервера PostgreSQL
DB_PORT	5432	Порт сервера PostgreSQL
DB_NAME	my_database	Имя базы данных
DB_USER	postgres	Имя пользователя
DB_PASSWORD	-	Пароль пользователя
Безопасность
Файл .env добавлен в .gitignore и не попадает в систему контроля версий

Пароли хранятся только в локальном файле .env

Рекомендуется использовать отдельного пользователя БД с ограниченными правами

Использование
Запуск приложения
bash
python app.py
Главное меню
После запуска отображается главное меню:

text
============================================================
Система управления базой данных v1.0.0
============================================================
1. Просмотреть всех пользователей
2. Добавить нового пользователя
3. Просмотреть все товары
4. Добавить новый товар
5. Статистика базы данных
6. Тестирование подключения к БД
7. Выход
============================================================
Описание функций
1. Просмотр пользователей
Отображает список всех пользователей в формате:

text
--- СПИСОК ПОЛЬЗОВАТЕЛЕЙ ---
ID    Имя пользователя    Email                Дата создания
--------------------------------------------------
1     john_doe           john@example.com     2024-01-15
2     jane_smith         jane@example.com     2024-01-15
2. Добавление пользователя
Запрашивает:

Имя пользователя (уникальное)

Email (уникальный)

Проверяет уникальность данных перед добавлением.

3. Просмотр товаров
Отображает каталог товаров:

text
--- КАТАЛОГ ТОВАРОВ ---
ID    Название            Цена     Описание
--------------------------------------------------
1     Ноутбук            $999.99   Высокопроизводительный...
2     Мышь               $29.99    Беспроводная мышь...
4. Добавление товара
Запрашивает:

Название товара

Цену (число)

Описание

5. Статистика базы данных
Показывает:

Количество пользователей

Количество товаров

Общую стоимость товаров

Среднюю цену товара

6. Тестирование подключения
Проверяет соединение с базой данных и показывает версию PostgreSQL.

Примеры использования
Добавление нового пользователя
text
Выберите опцию: 2

--- ДОБАВЛЕНИЕ НОВОГО ПОЛЬЗОВАТЕЛЯ ---
Введите имя пользователя: alex_ivanov
Введите email: alex@example.com
Пользователь успешно добавлен!
Просмотр статистики
text
Выберите опцию: 5

--- СТАТИСТИКА БАЗЫ ДАННЫХ ---
Пользователей: 5
Товаров: 8
Общая стоимость товаров: $2450.75
Средняя цена товара: $306.34
API документация
Класс DatabaseManager
Основной класс для работы с базой данных.

Методы
connect()
Устанавливает соединение с базой данных.

Возвращает: объект соединения или None при ошибке

Исключения: psycopg2.Error

create_tables()
Создает таблицы в базе данных.

Параметры: нет

Возвращает: нет

get_users()
Получает список всех пользователей.

Возвращает: список кортежей пользователей

Формат данных: (id, username, email, created_at)

add_user(username, email)
Добавляет нового пользователя.

Параметры:

username (str): имя пользователя

email (str): email адрес

Возвращает: bool (успех операции)

get_products()
Получает список всех товаров.

Возвращает: список кортежей товаров

Формат данных: (id, name, price, description, created_at)

add_product(name, price, description)
Добавляет новый товар.

Параметры:

name (str): название товара

price (float): цена товара

description (str): описание товара

Возвращает: bool (успех операции)

Класс DatabaseApp
Основной класс приложения.

Методы
run()
Запускает главный цикл приложения.

display_menu()
Отображает главное меню.

view_users()
Отображает список пользователей.

add_user()
Обрабатывает добавление нового пользователя.

view_products()
Отображает список товаров.

add_product()
Обрабатывает добавление нового товара.

show_statistics()
Отображает статистику базы данных.

test_connection()
Тестирует подключение к базе данных.

Модуль config
Класс Config
Управляет настройками приложения.

Свойства
DB_HOST: хост базы данных

DB_PORT: порт базы данных

DB_NAME: имя базы данных

DB_USER: пользователь БД

DB_PASSWORD: пароль БД

APP_NAME: название приложения

database_url (property)
Формирует URL для подключения к БД.

Разработка
Структура проекта
text
project/
├── app.py              # Основное приложение
├── database.py         # Работа с базой данных
├── config.py           # Конфигурация
├── requirements.txt    # Зависимости
├── .env               # Настройки (local)
├── .gitignore         # Исключения Git
└── README.md          # Документация
Стандарты кодирования
Имена классов: CamelCase (DatabaseManager)

Имена методов: snake_case (get_users)

Имена переменных: snake_case (user_count)

Константы: UPPER_CASE (DB_HOST)

Добавление новых функций
Пример: добавление функции удаления пользователя
Добавьте метод в DatabaseManager:

python
def delete_user(self, user_id):
    """Удаляет пользователя по ID"""
    conn = self.connect()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("DELETE FROM users WHERE id = %s", (user_id,))
            conn.commit()
            cur.close()
            return True
        except Exception as error:
            print(f"Ошибка удаления пользователя: {error}")
            return False
        finally:
            conn.close()
    return False
Добавьте обработчик в DatabaseApp:

python
def delete_user(self):
    """Удаление пользователя"""
    user_id = input("Введите ID пользователя для удаления: ")
    if self.db.delete_user(user_id):
        print("Пользователь успешно удален!")
    else:
        print("Ошибка удаления пользователя")
Обновите меню.

Тестирование
Создание тестов
python
# tests/test_database.py
import unittest
from database import DatabaseManager

class TestDatabase(unittest.TestCase):
    
    def setUp(self):
        self.db = DatabaseManager()
    
    def test_connection(self):
        self.assertIsNotNone(self.db.connect())
    
    def test_get_users(self):
        users = self.db.get_users()
        self.assertIsInstance(users, list)
Запуск тестов
bash
python -m unittest discover tests/
Устранение неисправностей
Распространенные проблемы
Ошибка подключения к базе данных
Симптомы:

text
Ошибка подключения: connection to server at "localhost" (::1), port 5432 failed
Решение:

Проверьте, запущен ли сервер PostgreSQL

Убедитесь в правильности параметров в .env

Проверьте существование базы данных

Ошибка аутентификации
Симптомы:

text
Ошибка подключения: password authentication failed for user "postgres"
Решение:

Проверьте пароль в файле .env

Попробуйте стандартный пароль 'postgres'

Сбросьте пароль через pgAdmin

Ошибка импорта модулей
Симптомы:

text
ModuleNotFoundError: No module named 'psycopg2'
Решение:

bash
pip install -r requirements.txt
Диагностика проблем
Проверка подключения к БД
python
from database import DatabaseManager
db = DatabaseManager()
db.test_connection()
Проверка структуры таблиц
sql
-- В pgAdmin выполните:
SELECT table_name 
FROM information_schema.tables 
WHERE table_schema = 'public';
Логирование
Приложение выводит информацию в консоль. Для добавления логирования в файл:

python
import logging

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
Часто задаваемые вопросы
Вопрос: Как изменить базу данных с PostgreSQL на другую СУБД?
Ответ: Требуется заменить psycopg2 на соответствующую библиотеку и обновить SQL запросы в database.py.

Вопрос: Можно ли использовать систему в production?
Ответ: Система предназначена для обучения и демонстрации. Для production использования требуется добавить аутентификацию, валидацию данных и обработку ошибок.

Вопрос: Как добавить новые таблицы?
Ответ: Добавьте SQL команды в метод create_tables() и создайте соответствующие методы в DatabaseManager.

Вопрос: Как сделать резервное копирование базы данных?
Ответ: Используйте pg_dump:

bash
pg_dump -h localhost -U postgres my_database > backup.sql
Вопрос: Как обновить схему базы данных?
Ответ: Создайте миграции или используйте ALTER TABLE команды.