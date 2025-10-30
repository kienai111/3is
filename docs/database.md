# Структура базы данных

## Обзор базы данных

Приложение использует **PostgreSQL** для хранения данных. База данных состоит из двух основных таблиц: `users` и `products`.

## Схема таблиц

### Таблица `users`

users
├── id (SERIAL, PRIMARY KEY) - Автоинкрементный идентификатор
├── username (VARCHAR(50), UNIQUE, NOT NULL) - Уникальное имя пользователя
├── email (VARCHAR(100), UNIQUE, NOT NULL) - Уникальный email
├── full_name (VARCHAR(100), NOT NULL) - Полное имя пользователя
├── created_at (TIMESTAMP) - Дата создания
└── updated_at (TIMESTAMP) - Дата последнего обновления


products
├── id (SERIAL, PRIMARY KEY) - Автоинкрементный идентификатор
├── name (VARCHAR(100), NOT NULL) - Название товара
├── description (TEXT) - Описание товара
├── price (DECIMAL(10,2)) - Цена (до 10 цифр, 2 после запятой)
├── stock_quantity (INTEGER) - Количество на складе
└── created_at (TIMESTAMP) - Дата добавления



## Фактические данные в базе

### Пользователи
| ID | Username | Email | Full Name | Created At |
|----|----------|-------|-----------|------------|
| 1 | john_doe | john@example.com | John Doe | 2025-10-14 15:56:32 |
| 2 | jane_smith | jane@example.com | Jane Smith | 2025-10-14 15:56:32 |
| 3 | bob_wilson | bob@example.com | Bob Wilson | 2025-10-14 15:56:32 |

### Товары
| ID | Name | Description | Price | Stock Quantity | Created At |
|----|------|-------------|-------|----------------|------------|
| 1 | Laptop | High-performance laptop | $999.99 | 10 | 2025-10-14 15:56:32 |
| 2 | Mouse | Wireless mouse | $29.99 | 50 | 2025-10-14 15:56:32 |
| 3 | Keyboard | Mechanical keyboard | $79.99 | 25 | 2025-10-14 15:56:32 |

## SQL команды создания таблиц (фактические)

### Таблица users
```sql
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

    Таблица products
CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10,2),
    stock_quantity INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

Типы данных PostgreSQL
SERIAL: Автоинкрементное целое число

VARCHAR(n): Строка переменной длины (max n символов)

DECIMAL(p,s): Число с фиксированной точностью (p - всего цифр, s - после запятой)

TEXT: Строка неограниченной длины

TIMESTAMP: Дата и время

INTEGER: Целое число

Ограничения (Constraints)
PRIMARY KEY: Уникальный идентификатор записи

UNIQUE: Гарантирует уникальность значения в столбце

NOT NULL: Запрещает пустые значения

DEFAULT: Значение по умолчанию

Примечания
База данных уже настроена и содержит тестовые данные

Все таблицы созданы и заполнены

Для работы приложения необходимо обновить код для поддержки полей full_name и stock_quantity


