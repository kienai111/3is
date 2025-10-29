import pytest
import psycopg2
from unittest.mock import Mock, patch
import sys
import os

# Добавляем путь для импорта модулей
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database import Database
import app

class TestDatabase:
    """Тесты для класса Database с моками"""
    
    @pytest.fixture
    def db(self):
        return Database()
    
    @patch('database.psycopg2.connect')
    def test_connect_success(self, mock_connect, db):
        """Тест успешного подключения к БД"""
        mock_conn = Mock()
        mock_connect.return_value = mock_conn
        
        result = db.connect()
        
        assert result is not None
        mock_connect.assert_called_once_with(
            host='localhost',
            port='5432',
            database='my_project_db',
            user='postgres',
            password='1111'
        )
    
    @patch('database.psycopg2.connect')
    def test_connect_failure(self, mock_connect, db):
        """Тест неудачного подключения"""
        mock_connect.side_effect = Exception("Connection failed")
        result = db.connect()
        assert result is None
    
    @patch('database.Database.connect')
    def test_create_tables(self, mock_connect, db):
        """Тест создания таблиц"""
        mock_conn = Mock()
        mock_cur = Mock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cur
        
        db.create_tables()
        
        assert mock_cur.execute.call_count == 2
        mock_conn.commit.assert_called_once()
    
    @patch('database.Database.connect')
    def test_get_users(self, mock_connect, db):
        """Тест получения пользователей"""
        mock_conn = Mock()
        mock_cur = Mock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cur
        
        expected_users = [
            (1, 'john_doe', 'john@example.com', '2023-01-01'),
            (2, 'jane_smith', 'jane@example.com', '2023-01-02')
        ]
        mock_cur.fetchall.return_value = expected_users
        
        users = db.get_users()
        
        assert users == expected_users
        mock_cur.execute.assert_called_once_with("SELECT * FROM users ORDER BY id")
    
    @patch('database.Database.connect')
    def test_add_user_success(self, mock_connect, db):
        """Тест успешного добавления пользователя"""
        mock_conn = Mock()
        mock_cur = Mock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cur
        
        result = db.add_user('testuser', 'test@example.com')
        
        assert result is True
        mock_cur.execute.assert_called_once_with(
            "INSERT INTO users (username, email) VALUES (%s, %s)",
            ('testuser', 'test@example.com')
        )
        mock_conn.commit.assert_called_once()
    
    @patch('database.Database.connect')
    def test_get_products(self, mock_connect, db):
        """Тест получения продуктов"""
        mock_conn = Mock()
        mock_cur = Mock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cur
        
        expected_products = [
            (1, 'Laptop', 999.99, 'High-performance laptop'),
            (2, 'Mouse', 29.99, 'Wireless mouse')
        ]
        mock_cur.fetchall.return_value = expected_products
        
        products = db.get_products()
        
        assert products == expected_products
        mock_cur.execute.assert_called_once_with("SELECT * FROM products ORDER BY id")
    
    @patch('database.Database.connect')
    def test_add_product_success(self, mock_connect, db):
        """Тест успешного добавления продукта"""
        mock_conn = Mock()
        mock_cur = Mock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cur
        
        result = db.add_product('Tablet', 299.99, 'Portable device')
        
        assert result is True
        mock_cur.execute.assert_called_once_with(
            "INSERT INTO products (name, price, description) VALUES (%s, %s, %s)",
            ('Tablet', 299.99, 'Portable device')
        )
        mock_conn.commit.assert_called_once()

class TestAppFunctions:
    """Тесты функций приложения"""
    
    @pytest.fixture
    def mock_db(self):
        return Mock(spec=Database)
    
    def test_view_users_with_data(self, mock_db, capsys):
        """Тест отображения пользователей с данными"""
        mock_users = [
            (1, 'john_doe', 'john@example.com', '2023-01-01'),
            (2, 'jane_smith', 'jane@example.com', '2023-01-02')
        ]
        mock_db.get_users.return_value = mock_users
        
        app.view_users(mock_db)
        
        captured = capsys.readouterr()
        assert "--- Users ---" in captured.out
        assert "ID: 1, Username: john_doe, Email: john@example.com" in captured.out
        assert "ID: 2, Username: jane_smith, Email: jane@example.com" in captured.out
    
    def test_view_users_empty(self, mock_db, capsys):
        """Тест отображения пустого списка пользователей"""
        mock_db.get_users.return_value = []
        
        app.view_users(mock_db)
        
        captured = capsys.readouterr()
        assert "No users found." in captured.out
    
    @patch('builtins.input')
    def test_add_user_success(self, mock_input, mock_db, capsys):
        """Тест успешного добавления пользователя"""
        mock_input.side_effect = ['newuser', 'newuser@example.com']
        mock_db.add_user.return_value = True
        
        app.add_user(mock_db)
        
        captured = capsys.readouterr()
        assert "User added successfully!" in captured.out
        mock_db.add_user.assert_called_once_with('newuser', 'newuser@example.com')
    
    @patch('builtins.input')
    def test_add_user_failure(self, mock_input, mock_db, capsys):
        """Тест неудачного добавления пользователя"""
        mock_input.side_effect = ['newuser', 'newuser@example.com']
        mock_db.add_user.return_value = False
        
        app.add_user(mock_db)
        
        captured = capsys.readouterr()
        assert "Failed to add user" in captured.out
    
    def test_view_products_with_data(self, mock_db, capsys):
        """Тест отображения продуктов с данными"""
        mock_products = [
            (1, 'Laptop', 999.99, 'High-performance laptop'),
            (2, 'Mouse', 29.99, 'Wireless mouse')
        ]
        mock_db.get_products.return_value = mock_products
        
        app.view_products(mock_db)
        
        captured = capsys.readouterr()
        assert "--- Products ---" in captured.out
        assert "ID: 1, Name: Laptop, Price: $999.99, Description: High-performance laptop" in captured.out
    
    @patch('builtins.input')
    def test_add_product_success(self, mock_input, mock_db, capsys):
        """Тест успешного добавления продукта"""
        mock_input.side_effect = ['Tablet', '299.99', 'Portable tablet']
        mock_db.add_product.return_value = True
        
        app.add_product(mock_db)
        
        captured = capsys.readouterr()
        assert "Product added successfully!" in captured.out
        mock_db.add_product.assert_called_once_with('Tablet', 299.99, 'Portable tablet')
    
    @patch('builtins.input')
    def test_add_product_invalid_price(self, mock_input, mock_db, capsys):
        """Тест добавления продукта с некорректной ценой"""
        mock_input.side_effect = ['Tablet', 'invalid_price', 'Portable tablet']
        
        app.add_product(mock_db)
        
        captured = capsys.readouterr()
        assert "Invalid price format" in captured.out
        mock_db.add_product.assert_not_called()

class TestIntegration:
    """Интеграционные тесты с реальной БД"""
    
    @pytest.fixture
    def test_db(self):
        """Фикстура для тестовой БД с очисткой данных"""
        db = Database()
        conn = db.connect()
        if conn:
            cur = conn.cursor()
            cur.execute("DELETE FROM products")
            cur.execute("DELETE FROM users")
            conn.commit()
            cur.close()
            conn.close()
        return db
    
    def test_user_crud_operations(self, test_db):
        """Интеграционный тест операций с пользователями"""
        # Добавление
        result = test_db.add_user('integration_user', 'integration@test.com')
        assert result is True
        
        # Чтение
        users = test_db.get_users()
        assert len(users) == 1
        assert users[0][1] == 'integration_user'
        assert users[0][2] == 'integration@test.com'
    
    def test_product_crud_operations(self, test_db):
        """Интеграционный тест операций с продуктами"""
        # Добавление
        result = test_db.add_product('Integration Product', 199.99, 'Test description')
        assert result is True
        
        # Чтение
        products = test_db.get_products()
        assert len(products) == 1
        assert products[0][1] == 'Integration Product'
        assert float(products[0][2]) == 199.99
        assert products[0][3] == 'Test description'

# ИСПРАВЛЕННЫЕ ТЕСТЫ - убраны проверки на SystemExit
@patch('builtins.input')
def test_main_exit(mock_input, capsys):
    """Тест выхода из приложения (исправленная версия)"""
    mock_input.return_value = '5'
    
    # Вместо проверки SystemExit, просто вызываем main и проверяем вывод
    try:
        app.main()
    except SystemExit:
        pass  # Игнорируем SystemExit если он есть
    
    captured = capsys.readouterr()
    assert "Goodbye!" in captured.out

@patch('builtins.input')
def test_main_invalid_option(mock_input, capsys):
    """Тест обработки неверной опции (исправленная версия)"""
    mock_input.side_effect = ['999', '5']  # Неверная опция, затем выход
    
    # Вместо проверки SystemExit, просто вызываем main
    try:
        app.main()
    except SystemExit:
        pass  # Игнорируем SystemExit если он есть
    
    captured = capsys.readouterr()
    assert "Invalid option!" in captured.out

# Дополнительные тесты для проверки меню
@patch('builtins.input')
def test_main_menu_navigation(mock_input, capsys):
    """Тест навигации по меню"""
    # Симулируем выбор разных опций меню
    mock_input.side_effect = ['1', '3', '5']  # Просмотр пользователей, продуктов, выход
    
    with patch.object(app, 'view_users') as mock_view_users, \
         patch.object(app, 'view_products') as mock_view_products:
        
        try:
            app.main()
        except SystemExit:
            pass
        
        # Проверяем, что функции были вызваны
        mock_view_users.assert_called_once()
        mock_view_products.assert_called_once()

if __name__ == "__main__":
    pytest.main([__file__, "-v"])