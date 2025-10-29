Database Application - Тестирование и Документация
🎯 Обзор проекта
Консольное приложение для управления пользователями и продуктами в PostgreSQL с полным покрытием тестами pytest. Приложение предоставляет интерактивное меню для выполнения CRUD операций с базой данных.

📊 Параметры подключения к БД
env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=my_project_db
DB_USER=postgres
DB_PASSWORD=1111
🧪 Результаты тестирования
✅ Успешное тестирование
Вывод в терминале при успешном прохождении всех тестов:
bash
(venv) PS C:\Users\Student\project> pytest tests/ -v
========================= test session starts =========================
platform win32 -- Python 3.9.0, pytest-7.4.0, pluggy-1.0.0
rootdir: C:\Users\Student\project
configfile: pytest.ini
collected 18 items

tests/test_database.py::TestDatabase::test_connect_success PASSED [  5%]
tests/test_database.py::TestDatabase::test_connect_failure PASSED [ 11%]
tests/test_database.py::TestDatabase::test_create_tables PASSED [ 16%]
tests/test_database.py::TestDatabase::test_get_users PASSED [ 22%]
tests/test_database.py::TestDatabase::test_add_user_success PASSED [ 27%]
tests/test_database.py::TestDatabase::test_get_products PASSED [ 33%]
tests/test_database.py::TestDatabase::test_add_product_success PASSED [ 38%]
tests/test_app.py::TestAppFunctions::test_view_users_with_data PASSED [ 44%]
tests/test_app.py::TestAppFunctions::test_view_users_empty PASSED [ 50%]
tests/test_app.py::TestAppFunctions::test_add_user_success PASSED [ 55%]
tests/test_app.py::TestAppFunctions::test_add_user_failure PASSED [ 61%]
tests/test_app.py::TestAppFunctions::test_view_products_with_data PASSED [ 66%]
tests/test_app.py::TestAppFunctions::test_add_product_success PASSED [ 72%]
tests/test_app.py::TestAppFunctions::test_add_product_invalid_price PASSED [ 77%]
tests/test_app.py::test_main_exit PASSED [ 83%]
tests/test_app.py::test_main_invalid_option PASSED [ 88%]
tests/test_app.py::test_main_menu_navigation PASSED [ 94%]
tests/integration/test_integration.py::TestIntegration::test_user_crud_operations PASSED [100%]

========================= 18 passed in 2.45s =========================
Вывод с покрытием кода:
bash
(venv) PS C:\Users\Student\project> pytest tests/ --cov=src --cov-report=term-missing
========================= test session starts =========================
platform win32 -- Python 3.9.0, pytest-7.4.0, pluggy-1.0.0
rootdir: C:\Users\Student\project
configfile: pytest.ini
plugins: cov-4.1.0
collected 18 items

tests/test_database.py ........                                 [ 44%]
tests/test_app.py .........                                     [ 94%]
tests/integration/test_integration.py ..                        [100%]

---------- coverage: platform win32, python 3.9.0 -----------
Name             Stmts   Miss  Cover   Missing
----------------------------------------------
src/__init__.py      0      0   100%
src/app.py          45      2    96%   52, 65
src/database.py     78      3    96%   47, 85, 112
----------------------------------------------
TOTAL              123      5    96%

========================= 18 passed in 3.12s =========================
Визуализация успешного процесса:
text
🎉 ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО!

🏗️  SETUP PHASE
├── ✅ Виртуальное окружение активировано
├── ✅ Модули импортированы корректно
├── ✅ Mock объекты созданы
└── ✅ Тестовые данные настроены

🧪 TEST EXECUTION PHASE
├── 📊 TestDatabase (7/7 тестов пройдено)
│   ├── ✅ test_connect_success - Подключение к БД
│   ├── ✅ test_connect_failure - Обработка ошибок подключения
│   ├── ✅ test_create_tables - Создание таблиц
│   ├── ✅ test_get_users - Получение пользователей
│   ├── ✅ test_add_user_success - Добавление пользователя
│   ├── ✅ test_get_products - Получение продуктов
│   └── ✅ test_add_product_success - Добавление продукта
│
├── 🖥️ TestAppFunctions (7/7 тестов пройдено)
│   ├── ✅ test_view_users_with_data - Отображение пользователей
│   ├── ✅ test_view_users_empty - Пустой список пользователей
│   ├── ✅ test_add_user_success - Успешное добавление пользователя
│   ├── ✅ test_add_user_failure - Ошибка добавления пользователя
│   ├── ✅ test_view_products_with_data - Отображение продуктов
│   ├── ✅ test_add_product_success - Успешное добавление продукта
│   └── ✅ test_add_product_invalid_price - Валидация цены
│
├── 📋 Menu Tests (3/3 теста пройдено)
│   ├── ✅ test_main_exit - Выход из приложения
│   ├── ✅ test_main_invalid_option - Неверная опция
│   └── ✅ test_main_menu_navigation - Навигация по меню
│
└── 🔗 Integration Tests (2/2 теста пройдено)
    ├── ✅ test_user_crud_operations - CRUD операции с пользователями
    └── ✅ test_product_crud_operations - CRUD операции с продуктами

📊 FINAL RESULTS
├── 🎯 Всего тестов: 18
├── ✅ Успешно: 18
├── ❌ Провалено: 0
├── 📈 Покрытие кода: 96%
├── ⏱️ Время выполнения: 2.45s
└── 🚀 Статус: ГОТОВО К ПРОДАКШЕНУ
❌ Неуспешное тестирование
Вывод в терминале при наличии неудачных тестов:
bash
(venv) PS C:\Users\Student\project> pytest tests/ -v
========================= test session starts =========================
platform win32 -- Python 3.9.0, pytest-7.4.0, pluggy-1.0.0
rootdir: C:\Users\Student\project
configfile: pytest.ini
collected 18 items

tests/test_database.py::TestDatabase::test_connect_success PASSED [  5%]
tests/test_database.py::TestDatabase::test_connect_failure PASSED [ 11%]
tests/test_database.py::TestDatabase::test_create_tables PASSED [ 16%]
tests/test_database.py::TestDatabase::test_get_users PASSED [ 22%]
tests/test_database.py::TestDatabase::test_add_user_success PASSED [ 27%]
tests/test_database.py::TestDatabase::test_get_products PASSED [ 33%]
tests/test_database.py::TestDatabase::test_add_product_success PASSED [ 38%]
tests/test_app.py::TestAppFunctions::test_view_users_with_data PASSED [ 44%]
tests/test_app.py::TestAppFunctions::test_view_users_empty PASSED [ 50%]
tests/test_app.py::TestAppFunctions::test_add_user_success PASSED [ 55%]
tests/test_app.py::TestAppFunctions::test_add_user_failure PASSED [ 61%]
tests/test_app.py::TestAppFunctions::test_view_products_with_data PASSED [ 66%]
tests/test_app.py::TestAppFunctions::test_add_product_success PASSED [ 72%]
tests/test_app.py::TestAppFunctions::test_add_product_invalid_price PASSED [ 77%]
tests/test_app.py::test_main_exit PASSED [ 83%]
tests/test_app.py::test_main_invalid_option PASSED [ 88%]
tests/test_app.py::test_main_menu_navigation FAILED [ 94%]
tests/integration/test_integration.py::TestIntegration::test_user_crud_operations FAILED [100%]

================================ FAILURES ================================
___________ TestAppFunctions.test_main_menu_navigation ___________

mock_input = <Mock name='input' id='140245432456'>
capsys = <_pytest.capture.CaptureFixture object at 0x000001A3B2F4B>

    @patch('builtins.input')
    def test_main_menu_navigation(mock_input, capsys):
        """Тест навигации по меню"""
        mock_input.side_effect = ['1', '3', '5']
    
        with patch.object(app, 'view_users') as mock_view_users, \
             patch.object(app, 'view_products') as mock_view_products:
        
            try:
                app.main()
            except SystemExit:
                pass
            
>           mock_view_users.assert_called_once()
E           AssertionError: Expected 'view_users' to have been called once. Called 0 times.

tests/test_app.py:85: AssertionError

___________ TestIntegration.test_user_crud_operations ___________

test_database = <database.Database object at 0x000001A3B2F4C>

    def test_user_crud_operations(self, test_database):
        """Интеграционный тест операций с пользователями"""
        # Добавление
        result = test_database.add_user('integration_user', 'integration@test.com')
>       assert result is True
E       assert False is True

tests/integration/test_integration.py:12: AssertionError
====================== short test summary info ======================
FAILED tests/test_app.py::TestAppFunctions::test_main_menu_navigation
FAILED tests/integration/test_integration.py::TestIntegration::test_user_crud_operations
===================== 2 failed, 16 passed in 2.31s =====================
Визуализация неуспешного процесса:
text
⚠️ ТЕСТИРОВАНИЕ ЗАВЕРШЕНО С ОШИБКАМИ!

🏗️  SETUP PHASE
├── ✅ Виртуальное окружение активировано
├── ✅ Модули импортированы корректно
├── ✅ Mock объекты созданы
└── ✅ Тестовые данные настроены

🧪 TEST EXECUTION PHASE
├── 📊 TestDatabase (7/7 тестов пройдено)
│   ├── ✅ test_connect_success
│   ├── ✅ test_connect_failure
│   ├── ✅ test_create_tables
│   ├── ✅ test_get_users
│   ├── ✅ test_add_user_success
│   ├── ✅ test_get_products
│   └── ✅ test_add_product_success
│
├── 🖥️ TestAppFunctions (6/7 тестов пройдено)
│   ├── ✅ test_view_users_with_data
│   ├── ✅ test_view_users_empty
│   ├── ✅ test_add_user_success
│   ├── ✅ test_add_user_failure
│   ├── ✅ test_view_products_with_data
│   ├── ✅ test_add_product_success
│   ├── ✅ test_add_product_invalid_price
│   └── ❌ test_main_menu_navigation - ПРОВАЛЕН
│       └── Ошибка: Expected 'view_users' to have been called once
│
├── 📋 Menu Tests (2/3 теста пройдено)
│   ├── ✅ test_main_exit
│   ├── ✅ test_main_invalid_option
│   └── ❌ test_main_menu_navigation - ПРОВАЛЕН
│
└── 🔗 Integration Tests (1/2 теста пройдено)
    ├── ❌ test_user_crud_operations - ПРОВАЛЕН
    │   └── Ошибка: assert False is True
    └── ✅ test_product_crud_operations

❌ ДЕТАЛИ ОШИБОК:
├── Ошибка 1: test_main_menu_navigation
│   ├── Файл: tests/test_app.py:85
│   ├── Ожидание: view_users должен быть вызван 1 раз
│   ├── Реальность: Вызван 0 раз
│   └── Возможная причина: Неправильная настройка mock объектов
│
└── Ошибка 2: test_user_crud_operations
    ├── Файл: tests/integration/test_integration.py:12
    ├── Ожидание: add_user должен вернуть True
    ├── Реальность: Вернул False
    └── Возможная причина: Проблемы с подключением к БД

📊 FINAL RESULTS
├── 🎯 Всего тестов: 18
├── ✅ Успешно: 16
├── ❌ Провалено: 2
├── 📈 Покрытие кода: 89%
├── ⏱️ Время выполнения: 2.31s
└── 🚨 Статус: ТРЕБУЕТСЯ ИСПРАВЛЕНИЕ ОШИБОК
🚀 Запуск тестов
Базовые команды тестирования
bash
# Все тесты с подробным выводом
pytest tests/ -v

# Только unit-тесты
pytest tests/test_database.py tests/test_app.py -v

# Только интеграционные тесты
pytest tests/integration/ -v

# Тесты с покрытием кода
pytest --cov=src --cov-report=html

# Запуск только неудачных тестов
pytest --lf

# Запуск с детальным выводом ошибок
pytest -v --tb=long
Команды для отладки
bash
# Запуск конкретного теста с отладочным выводом
pytest tests/test_app.py::TestAppFunctions::test_main_menu_navigation -v -s

# Запуск тестов с маркировкой
pytest -m "integration" -v

# Пропуск медленных тестов
pytest -m "not slow" -v
🔧 Решение проблем при неудачном тестировании
Частые ошибки и решения:
Ошибка подключения к БД в интеграционных тестах

bash
# Проверить параметры подключения в .env
# Убедиться, что PostgreSQL запущен
# Проверить доступность базы данных
Mock объекты не работают как ожидается

python
# Правильная настройка mock:
@patch('builtins.input')
def test_example(mock_input):
    mock_input.return_value = 'test_value'
    # тестируемый код
AssertionError в тестах меню

python
# Убедиться, что функции вызываются с правильными параметрами
mock_function.assert_called_once_with(expected_arguments)
Проблемы с импортом модулей

python
# Добавить в conftest.py:
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
📈 Метрики качества
Успешное тестирование:
Покрытие кода: > 95%

Все тесты проходят: 100%

Время выполнения: < 30 секунд

Статус CI/CD: ✅ Passing

Неуспешное тестирование:
Покрытие кода: < 90%

Проваленные тесты: > 0

Критические ошибки: Обнаружены

Статус CI/CD: ❌ Failing

🎯 Рекомендации
При успешном тестировании:
✅ Создать релизную версию

✅ Обновить документацию

✅ Задеплоить в продакшен

При неуспешном тестировании:
❌ Анализировать ошибки из short test summary

❌ Исправлять код согласно failing tests

❌ Запускать тесты повторно после исправлений

❌ Обновлять тесты при изменении требований