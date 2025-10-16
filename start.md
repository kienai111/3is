# Руководство по началу работы

## Быстрый старт за 5 шагов

### Шаг 1: Установите Python
1. Скачайте Python с официального сайта: **https://python.org**
2. Запустите установщик
3. **ВАЖНО:** Отметьте галочку "Add Python to PATH"
4. Нажмите "Install Now"

**Проверка установки:**
```bash
python --version

Должна появиться версия Python (например, Python 3.11.0)

## Шаг 2: Установите PostgreSQL

Скачайте PostgreSQL: https://postgresql.org/download/

Запустите установщик

Запомните пароль для пользователя postgres (он понадобится позже)

Завершите установку

## Шаг 3: Скачайте проект

# Способ 1: Через Git
git clone https://github.com/username/ваш-проект.git
cd ваш-проект

# Способ 2: Скачайте ZIP
# На GitHub нажмите "Code" → "Download ZIP"
# Распакуйте архив в нужную папку

Шаг 4: Настройте проект

1. Откройте папку проекта в VS Code

2. Создайте файл .env в корне проекта

3. Добавьте в него:
 .env
 DB_HOST=localhost
DB_PORT=5432
DB_NAME=my_project_db
DB_USER=postgres
DB_PASSWORD=1111

Шаг 5: Запустите проект

# Установите зависимости
pip install -r requirements.txt

# Создайте базу данных
python database.py

# Запустите приложение
python app.py

Что нужно установить (список)
Обязательные программы:
Python (с сайта python.org)

PostgreSQL (с сайта postgresql.org)

VS Code (или другой редактор кода)

Файлы проекта:
app.py - главная программа

database.py - настройка базы данных

config.py - настройки

requirements.txt - список библиотек

.env - ваши настройки (создать)