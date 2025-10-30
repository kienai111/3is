# Руководство по использованию

## Запуск приложения

```bash
python app.py
После успешного запуска вы увидите главное меню:

text
🚀 Database Application

1. View users
2. Add user
3. View products
4. Add product
5. Exit

Choose option:
Основные функции
📊 Просмотр пользователей (Опция 1)
Что делает: Отображает список всех пользователей из базы данных

Пример вывода:

text
--- Users ---
ID: 1, Username: john_doe, Email: john@example.com, Created: 2025-10-14 15:56:32
ID: 2, Username: jane_smith, Email: jane@example.com, Created: 2025-10-14 15:56:32
ID: 3, Username: bob_wilson, Email: bob@example.com, Created: 2025-10-14 15:56:32
Особенности:

Если пользователей нет, показывает "No users found."

Отображает только базовые поля (username, email, created_at)

⚠️ Не отображает поля full_name и updated_at (доступны в БД)

👥 Добавление пользователя (Опция 2)
Что делает: Добавляет нового пользователя в базу данных

Процесс:

text
➕ Add New User
Username: alice_brown
Email: alice@example.com
✅ User added successfully!
Требуемые данные:

Username - уникальное имя пользователя (максимум 50 символов)

Email - уникальный email адрес (максимум 100 символов)

Валидация:

Проверяет уникальность имени пользователя

Проверяет уникальность email

⚠️ Не запрашивает поле full_name (обязательное в БД)

Возможные результаты:

✅ User added successfully! - пользователь добавлен

❌ Failed to add user. Username might already exist. - ошибка добавления

🛍️ Просмотр товаров (Опция 3)
Что делает: Отображает список всех товаров из базы данных

Пример вывода:

text
--- Products ---
ID: 1, Name: Laptop, Price: $999.99, Description: High-performance laptop
ID: 2, Name: Mouse, Price: $29.99, Description: Wireless mouse
ID: 3, Name: Keyboard, Price: $79.99, Description: Mechanical keyboard
Особенности:

Если товаров нет, показывает "No products found."

Форматирует цену в долларовом формате ($29.99)

⚠️ Не отображает поле stock_quantity (доступно в БД)

📦 Добавление товара (Опция 4)
Что делает: Добавляет новый товар в базу данных

Процесс:

text
➕ Add New Product
Name: Monitor
Price: 299.99
Description: 24-inch LED monitor
✅ Product added successfully!
Требуемые данные:

Name - название товара (максимум 100 символов)

Price - цена товара (должна быть числом)

Description - описание товара

Валидация:

Проверяет что цена является корректным числом

⚠️ Не запрашивает поле stock_quantity (доступно в БД)

Возможные результаты:

✅ Product added successfully! - товар добавлен

❌ Failed to add product. - ошибка добавления

❌ Invalid price format. Please enter a number. - неверный формат цены

🚪 Выход (Опция 5)
Что делает: Завершает работу приложения

Сообщение: 👋 Goodbye!

Полный пример сессии работы
text
🚀 Database Application

1. View users
2. Add user
3. View products
4. Add product
5. Exit

Choose option: 1

--- Users ---
ID: 1, Username: john_doe, Email: john@example.com, Created: 2025-10-14 15:56:32
ID: 2, Username: jane_smith, Email: jane@example.com, Created: 2025-10-14 15:56:32
ID: 3, Username: bob_wilson, Email: bob@example.com, Created: 2025-10-14 15:56:32

Choose option: 2

➕ Add New User
Username: mike_johnson
Email: mike@example.com
✅ User added successfully!

Choose option: 1

--- Users ---
ID: 1, Username: john_doe, Email: john@example.com, Created: 2025-10-14 15:56:32
ID: 2, Username: jane_smith, Email: jane@example.com, Created: 2025-10-14 15:56:32
ID: 3, Username: bob_wilson, Email: bob@example.com, Created: 2025-10-14 15:56:32
ID: 4, Username: mike_johnson, Email: mike@example.com, Created: 2025-10-14 16:00:15

Choose option: 4

➕ Add New Product
Name: Headphones
Price: 149.99
Description: Wireless noise-canceling headphones
✅ Product added successfully!

Choose option: 5
👋 Goodbye!
Обработка ошибок
Некорректный выбор опции
text
Choose option: 6
❌ Invalid option!
Некорректный формат цены
text
➕ Add New Product
Name: Test Product
Price: not_a_number
❌ Invalid price format. Please enter a number.
Проблемы с базой данных
text
❌ Connection error: connection to server at "localhost" (::1), port 5432 failed
Ошибка при добавлении пользователя
text
➕ Add New User
Username: john_doe  # уже существует
Email: new@example.com
❌ Failed to add user. Username might already exist.
Особенности работы с текущей структурой БД
Расхождения между кодом и базой данных
Пользователи:

✅ Код использует: username, email

📋 База данных содержит: username, email, full_name, created_at, updated_at

⚠️ Поле full_name не заполняется при добавлении пользователя

Товары:

✅ Код использует: name, price, description

📋 База данных содержит: name, price, description, stock_quantity, created_at

⚠️ Поле stock_quantity не заполняется при добавлении товара

Рекомендации по использованию
Для просмотра полных данных используйте прямое подключение к PostgreSQL

При добавлении пользователей учитывайте, что поле full_name будет пустым

При добавлении товаров поле stock_quantity будет иметь значение NULL

Для production использования рекомендуется обновить код для поддержки всех полей

Советы по эффективной работе
Быстрая навигация
Используйте цифры 1-5 для выбора опций

Приложение работает в бесконечном цикле до выбора опции 5

Работа с данными
Все данные автоматически сохраняются в базе данных

Временные метки создаются автоматически

Уникальные поля (username, email) защищены от дублирования

Отладка проблем
При ошибках подключения проверьте файл .env

При проблемах с данными проверьте логи PostgreSQL

Для сложных операций используйте прямое подключение к БД

Следующие шаги
После освоения базовых функций рекомендуется:

🛠️ Обновить код для поддержки всех полей базы данных

📊 Добавить новые функции: удаление, редактирование, поиск

🔍 Изучить API в файле api-reference.md для глубокого понимания

🧪 Протестировать приложение с помощью pytest test_app.py -v