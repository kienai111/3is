# Справочник API

## Класс Database (`database.py`)

Основной класс для работы с PostgreSQL базой данных.

### `__init__(self)`
**Инициализация объекта базы данных**
- Создает экземпляр класса, но не подключается к БД
- Подключение происходит при первом вызове методов

### `connect(self) -> psycopg2.Connection`
**Подключение к PostgreSQL**
- Использует параметры из `.env` файла
- **Возвращает**: Объект соединения или None при ошибке
- **Сообщения**: "✅ Connected to PostgreSQL successfully!" или "❌ Connection error: {e}"

### `create_tables(self) -> None`
**Создание таблиц в базе данных**
- Создает таблицы `users` и `products` если они не существуют
- **Структура users**: id, username, email, full_name, created_at, updated_at
- **Структура products**: id, name, price, description, stock_quantity, created_at

### `insert_sample_data(self) -> None`
**Добавление тестовых данных**
- Пользователи: john_doe, jane_smith, bob_wilson с полными именами
- Товары: Laptop ($999.99), Mouse ($29.99), Keyboard ($79.99) с количеством на складе

### `get_users(self) -> List[Tuple]`
**Получение всех пользователей**
- **SQL запрос**: `SELECT * FROM users ORDER BY id`
- **Возвращает**: Список кортежей `[(id, username, email, full_name, created_at, updated_at), ...]`
- **Сортировка**: По ID в возрастающем порядке
- **При ошибке**: Возвращает пустой список `[]`

### `get_products(self) -> List[Tuple]`
**Получение всех товаров**
- **SQL запрос**: `SELECT * FROM products ORDER BY id`
- **Возвращает**: Список кортежей `[(id, name, description, price, stock_quantity, created_at), ...]`
- **Сортировка**: По ID в возрастающем порядке

### `add_user(self, username: str, email: str) -> bool`
**Добавление нового пользователя**
- **SQL запрос**: `INSERT INTO users (username, email) VALUES (%s, %s)`
- **Параметры**:
  - `username`: Уникальное имя пользователя (VARCHAR(50))
  - `email`: Уникальный email (VARCHAR(100))
- **Возвращает**: `True` при успехе, `False` при ошибке
- **Валидация**: Уникальность username и email
- **⚠️ Внимание**: Не заполняет поле `full_name` (требует обновления)

### `add_product(self, name: str, price: float, description: str) -> bool`
**Добавление нового товара**
- **SQL запрос**: `INSERT INTO products (name, price, description) VALUES (%s, %s, %s)`
- **Параметры**:
  - `name`: Название товара (VARCHAR(100))
  - `price`: Цена (DECIMAL(10,2))
  - `description`: Описание (TEXT)
- **Возвращает**: `True` при успехе, `False` при ошибке
- **⚠️ Внимание**: Не заполняет поле `stock_quantity` (требует обновления)

## Функции приложения (`app.py`)

### `main() -> None`
**Главная функция приложения**
- Создает экземпляр Database
- Запускает основной цикл меню
- Обрабатывает пользовательский ввод
- **Цикл меню**: Бесконечный цикл до выбора опции "5. Exit"

### `view_users(db: Database) -> None`
**Отображение списка пользователей**
- Получает данные через `db.get_users()`
- Форматирует вывод: `ID: {user[0]}, Username: {user[1]}, Email: {user[2]}, Created: {user[3]}`
- **⚠️ Внимание**: Не отображает поля `full_name` и `updated_at`

### `add_user(db: Database) -> None`
**Добавление пользователя через интерфейс**
- Запрашивает username и email у пользователя
- Вызывает `db.add_user()`
- Показывает результат: "✅ User added successfully!" или "❌ Failed to add user"
- **⚠️ Внимание**: Не запрашивает `full_name`

### `view_products(db: Database) -> None`
**Отображение списка товаров**
- Получает данные через `db.get_products()`
- Форматирует вывод: `ID: {product[0]}, Name: {product[1]}, Price: ${product[2]}, Description: {product[3]}`
- **⚠️ Внимание**: Не отображает поле `stock_quantity`

### `add_product(db: Database) -> None`
**Добавление товара через интерфейс**
- Запрашивает name, price, description
- Валидирует числовой формат цены (try/except ValueError)
- Вызывает `db.add_product()`
- Показывает результат: "✅ Product added successfully!" или "❌ Failed to add product"
- **⚠️ Внимание**: Не запрашивает `stock_quantity`

## Расхождения между кодом и структурой БД

### Пользователи
| Поле в БД | Используется в коде | Статус |
|-----------|---------------------|---------|
| id | ✅ Да | Полная поддержка |
| username | ✅ Да | Полная поддержка |
| email | ✅ Да | Полная поддержка |
| full_name | ❌ Нет | Требует добавления |
| created_at | ✅ Да | Полная поддержка |
| updated_at | ❌ Нет | Требует добавления |

### Товары
| Поле в БД | Используется в коде | Статус |
|-----------|---------------------|---------|
| id | ✅ Да | Полная поддержка |
| name | ✅ Да | Полная поддержка |
| description | ✅ Да | Полная поддержка |
| price | ✅ Да | Полная поддержка |
| stock_quantity | ❌ Нет | Требует добавления |
| created_at | ✅ Да | Полная поддержка |

## Рекомендации по обновлению API

1. **Обновить `add_user()`** - добавить параметр `full_name`
2. **Обновить `view_users()`** - отображать `full_name` и `updated_at`
3. **Обновить `add_product()`** - добавить параметр `stock_quantity`
4. **Обновить `view_products()`** - отображать `stock_quantity`
5. **Добавить методы обновления** для `updated_at` поля