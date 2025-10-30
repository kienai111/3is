# Установка и настройка

## Предварительные требования

- **Python 3.8** или выше
- **PostgreSQL 12** или выше
- **pip** (менеджер пакетов Python)
- **Доступ к базе данных** с правами на создание таблиц

## Установка зависимостей

### 1. Активация виртуального окружения
```bash
# Если виртуальное окружение еще не создано
python -m venv .venv

# Активация для Windows
.venv\Scripts\activate

# Активация для Linux/Mac
source .venv/bin/activate

2. Установка пакетов Python
pip install -r requirements.txt

3. Содержимое файла requirements.txt:
psycopg2-binary==2.9.6
python-dotenv==1.0.0
pytest==7.4.0

Настройка подключения к базе данных
1. Создание файла окружения
Создайте файл .env в корневой папке проекта:
DB_HOST=localhost
DB_PORT=5432
DB_NAME=mydatabase
DB_USER=your_username
DB_PASSWORD=your_password

2. Настройка параметров подключения
DB_HOST: Адрес сервера PostgreSQL (обычно localhost)

DB_PORT: Порт PostgreSQL (по умолчанию 5432)

DB_NAME: Имя базы данных

DB_USER: Имя пользователя PostgreSQL

DB_PASSWORD: Пароль пользователя

Инициализация базы данных
Вариант 1: Использование существующей базы
Если база данных уже создана и содержит таблицы:
# Просто запустите приложение
python app.py

Проверка установки
1. Проверка подключения к базе данных
python -c "
from database import Database
db = Database()
conn = db.connect()
if conn:
    print('✅ Успешное подключение к базе данных')
    conn.close()
else:
    print('❌ Ошибка подключения')
"
2. Проверка существующих данных
python -c "
from database import Database
db = Database()
users = db.get_users()
products = db.get_products()
print(f'✅ Найдено пользователей: {len(users)}')
print(f'✅ Найдено товаров: {len(products)}')
"
3. Запуск приложения
python app.py

Ожидаемый результат:
🚀 Database Application

1. View users
2. Add user
3. View products
4. Add product
5. Exit

Choose option:

Устранение неполадок
Ошибка подключения к PostgreSQL
❌ Connection error: connection to server at "localhost" (::1), port 5432 failed
Решение: Убедитесь, что PostgreSQL запущен и доступен

Ошибка аутентификации
❌ Connection error: password authentication failed for user "your_username"
Решение: Проверьте правильность DB_USER и DB_PASSWORD в файле .env

Ошибка базы данных
❌ Connection error: database "mydatabase" does not exist

Решение: Создайте базу данных в PostgreSQL или укажите существующую

Ошибка импорта модулей
ModuleNotFoundError: No module named 'psycopg2'
Решение: Убедитесь, что зависимости установлены: pip install -r requirements.txt

Структура базы данных после установки
После успешной установки в вашей базе данных будут:

Таблица users
3 тестовых пользователя с полными именами

Поля: id, username, email, full_name, created_at, updated_at

Таблица products
3 тестовых товара с количеством на складе

Поля: id, name, description, price, stock_quantity, created_at

Следующие шаги
После успешной установки:

🎯 Ознакомьтесь с руководством по использованию в usage.md

🔧 Изучите API приложения в api-reference.md

🧪 Запустите тесты: pytest test_app.py -v

📝 При необходимости обновите код для поддержки всех полей базы данных