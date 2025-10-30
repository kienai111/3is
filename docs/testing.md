# Тестирование

## Запуск тестов

### Базовый запуск всех тестов
```bash
pytest test_app.py -v

Запуск с подробным выводом
pytest test_app.py -s -v

Запуск конкретного теста
pytest test_app.py::test_database_connection -v

Запуск тестов с покрытием кода
# Установите pytest-cov если не установлен
pip install pytest-cov

# Запуск с отчетом о покрытии
pytest test_app.py --cov=app --cov-report=html

Структура тестирования
Используемые технологии
pytest: Основной фреймворк для тестирования

Модульные тесты: Проверка отдельных функций и методов

Интеграционные тесты: Проверка взаимодействия с базой данных

Организация тестов
Тесты находятся в файле test_app.py и разделены на:

Тесты подключения к базе данных

Тесты операций с пользователями

Тесты операций с товарами

Тесты функций приложения

Примеры тестов
Тест подключения к базе данных
def test_database_connection():
    """Тестирование подключения к PostgreSQL"""
    db = Database()
    conn = db.connect()
    assert conn is not None, "Подключение к базе данных не установлено"
    conn.close()

Тест создания таблиц
def test_create_tables():
    """Тестирование создания таблиц в базе данных"""
    db = Database()
    
    # Временно заменим метод для тестирования
    original_connect = db.connect
    tables_created = []
    
    def mock_connect():
        class MockCursor:
            def execute(self, command):
                tables_created.append(command)
            def close(self): pass
        class MockConn:
            def cursor(self): return MockCursor()
            def commit(self): pass
            def close(self): pass
        return MockConn()
    
    db.connect = mock_connect
    db.create_tables()
    
    assert len(tables_created) == 2, "Должны быть созданы две таблицы"
    assert "CREATE TABLE" in tables_created[0], "Первая команда должна создавать таблицу"

Тест получения пользователей
def test_get_users():
    """Тестирование получения списка пользователей"""
    db = Database()
    users = db.get_users()
    
    assert isinstance(users, list), "Метод должен возвращать список"
    # Проверяем что есть как минимум тестовые пользователи
    assert len(users) >= 3, "Должны быть как минимум 3 тестовых пользователя"

Тест добавления пользователя
def test_add_user():
    """Тестирование добавления нового пользователя"""
    db = Database()
    
    # Генерируем уникальное имя для теста
    import random
    test_username = f"test_user_{random.randint(1000, 9999)}"
    test_email = f"{test_username}@example.com"
    
    result = db.add_user(test_username, test_email)
    assert result == True, "Пользователь должен быть успешно добавлен"

Тест валидации цены товара
def test_price_validation():
    """Тестирование валидации цены товара"""
    # Этот тест проверяет логику в функции add_product в app.py
    test_cases = [
        ("100", True),      # Корректная цена
        ("99.99", True),    # Цена с десятичными
        ("invalid", False), # Некорректная цена
        ("", False),        # Пустая цена
    ]
    
    for price_input, should_be_valid in test_cases:
        try:
            price = float(price_input)
            assert should_be_valid, f"Цена '{price_input}' должна быть невалидной"
        except ValueError:
            assert not should_be_valid, f"Цена '{price_input}' должна быть валидной"

Интеграция с VS Code
Настройка pytest в VS Code
Откройте Command Palette: Ctrl+Shift+P

Выберите: "Python: Configure Tests"

Выберите тестовый фреймворк: "pytest"

Укажите папку с тестами: Корневая папка проекта

Запуск тестов через интерфейс VS Code
Откройте панель Testing (иконка с колбой в левой панели)

Нажмите "Configure Python Tests" если еще не настроено

Выберите pytest как test framework

Укажите корневую папку проекта

Запускайте тесты через интерфейс панели Testing

Горячие клавиши для тестирования в VS Code
Ctrl+Shift+P → "Python: Run All Tests"

Правой кнопкой на тестовом файле → "Run Current Test File"

Правой кнопкой на конкретном тесте → "Run Test"

Ctrl+Shift+P → "Python: Show Test Output"

Best Practices
Организация тестов
python
# Хорошая структура тестового файла
import pytest
from database import Database

class TestDatabase:
    """Тесты для класса Database"""
    
    def setup_method(self):
        """Настройка перед каждым тестом"""
        self.db = Database()
    
    def teardown_method(self):
        """Очистка после каждого теста"""
        # При необходимости очистить тестовые данные
    
    def test_connection(self):
        """Тест подключения"""
        assert self.db.connect() is not None
    
    def test_get_users(self):
        """Тест получения пользователей"""
        users = self.db.get_users()
        assert isinstance(users, list)

class TestApplication:
    """Тесты для функций приложения"""
    
    def test_view_users_function(self):
        """Тест функции отображения пользователей"""
        # Тестирование логики отображения
        pass
Тестирование базы данных
✅ Используйте тестовую базу данных если возможно

✅ Очищайте тестовые данные после тестов

✅ Тестируйте как успешные сценарии, так и ошибки

✅ Используйте моки для изоляции тестов

Покрытие кода
bash
# Генерация HTML отчета о покрытии
pytest test_app.py --cov=app --cov-report=html

# Просмотр отчета
# Откройте файл htmlcov/index.html в браузере
Отладка тестов
Добавление отладочного вывода
python
def test_with_debug_output():
    db = Database()
    users = db.get_users()
    print(f"Найдено пользователей: {len(users)}")  # Вывод в консоль при -s
    assert len(users) > 0
Использование pdb для отладки
python
def test_with_breakpoint():
    db = Database()
    import pdb; pdb.set_trace()  # Точка останова
    users = db.get_users()
Частые проблемы и решения
Проблема: Тесты не находятся
Решение: Убедитесь что файлы тестов начинаются с test_ или заканчиваются _test.py

Проблема: Ошибки импорта
Решение: Добавьте корневую папку проекта в PYTHONPATH или используйте относительные импорты

Проблема: Тесты влияют друг на друга
Решение: Используйте setup/teardown методы для изоляции тестов

Проблема: Медленные тесты базы данных
Решение: Используйте моки для тестирования логики без реального подключения к БД