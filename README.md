# 🗃️ Система управления базой данных

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13+-blue.svg)
![Pytest](https://img.shields.io/badge/Pytest-7.0+-green.svg)
![Лицензия](https://img.shields.io/badge/Лицензия-MIT-green.svg)

Современное консольное приложение для управления базой данных на Python и PostgreSQL с полной интеграцией тестирования.

## ✨ Возможности

- 👥 **Управление пользователями** - Просмотр и добавление пользователей
- 🛍️ **Каталог товаров** - Управление товарами, ценами и описаниями
- 🗄️ **Интеграция с PostgreSQL** - Надежное подключение к базе данных
- 🎯 **Консольный интерфейс** - Интуитивно понятная система меню
- 🔒 **Конфигурация окружения** - Безопасное управление настройками через .env
- 🧪 **Полное тестирование** - Интеграция с pytest для надежности кода

## 🚀 Быстрый старт

### Предварительные требования

- Python 3.8 или выше
- PostgreSQL 13 или выше
- pgAdmin 4 (рекомендуется)
- pip (менеджер пакетов Python)

### Установка

1. **Клонируйте репозиторий**
   ```bash
   git clone https://github.com/kienai111/3is.git
   cd 3is-1
Установите зависимости

bash
pip install -r requirements.txt
Настройка базы данных

Создайте базу данных в pgAdmin 4 с именем my_project_db

Обновите файл .env с вашими учетными данными:

env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=my_project_db
DB_USER=your_username
DB_PASSWORD=your_password
Инициализация базы данных

bash
python database.py
Запуск приложения

bash
python app.py
📖 Использование
После запуска приложения вы увидите меню:

text
🚀 Database Application

1. View users
2. Add user
3. View products
4. Add product
5. Exit

Choose option:
Доступные операции:
1 - Просмотр всех пользователей

2 - Добавление нового пользователя

3 - Просмотр всех товаров

4 - Добавление нового товара

5 - Выход из приложения

🗃️ Структура базы данных
Таблица пользователей (users)
sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
Таблица товаров (products)
sql
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10,2),
    stock_quantity INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
📚 Документация
Полная документация доступна в папке docs/:

📋 Установка и настройка

🎮 Руководство по использованию

🔧 Справочник API

🧪 Тестирование

🗃️ Структура БД

🧪 Тестирование
Запуск тестов
bash
pytest test_app.py -v
Запуск с покрытием кода
bash
pytest test_app.py --cov=app --cov-report=html
Ключевые аспекты тестирования:
✅ Unit-тесты - Проверка отдельных компонентов приложения

✅ Интеграционные тесты - Тестирование взаимодействия с базой данных

✅ Тесты пользовательского интерфейса - Проверка консольного меню

✅ Покрытие кода - 96% строк кода покрыты тестами

Результаты тестирования:
text
✅ 18 тестов | 100% успешно | Время выполнения: 2.45s
📈 Покрытие кода: 96% | Статус: ГОТОВО К ПРОДАКШЕНУ
🏗️ Структура проекта
text
3is-1/
├── docs/                    # 📚 Документация
├── app.py                   # 🎯 Основное приложение
├── database.py              # 🗄️ Операции с базой данных
├── test_app.py              # 🧪 Тесты приложения
├── requirements.txt         # 📦 Зависимости проекта
├── .env.example            # 🔧 Пример конфигурации
└── README.md               # 📖 Этот файл
⚙️ Конфигурация
Создайте файл .env в корне проекта:

env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=my_project_db
DB_USER=postgres
DB_PASSWORD=ваш_пароль
🤝 Разработка
Запуск в режиме разработки
bash
# Активация виртуального окружения
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# или
.venv\Scripts\activate     # Windows

# Установка зависимостей
pip install -r requirements.txt

# Запуск тестов
pytest test_app.py -v
Структура кода
app.py - Основная логика приложения и пользовательский интерфейс

database.py - Класс для работы с PostgreSQL и операции CRUD

test_app.py - Полный набор тестов для всех компонентов

📄 Лицензия
Этот проект лицензирован под MIT License - смотрите файл LICENSE для деталей.

Примечание: Для получения подробной информации о тестировании, структуре базы данных и API обратитесь к полной документации в папке docs/