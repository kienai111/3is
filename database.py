import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self):
        self.conn = None
    
    def connect(self):
        """Connect to PostgreSQL database"""
        try:
            self.conn = psycopg2.connect(
                host=os.getenv('DB_HOST'),
                port=os.getenv('DB_PORT'),
                database=os.getenv('DB_NAME'),
                user=os.getenv('DB_USER'),
                password=os.getenv('DB_PASSWORD')
            )
            print("✅ Connected to PostgreSQL successfully!")
            return self.conn
        except Exception as e:
            print(f"❌ Connection error: {e}")
            return None
    
    def create_tables(self):
        """Create database tables"""
        commands = (
            """
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS products (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                price DECIMAL(10,2),
                description TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        
        conn = self.connect()
        if conn:
            try:
                cur = conn.cursor()
                for command in commands:
                    cur.execute(command)
                conn.commit()
                cur.close()
                print("✅ Tables created successfully!")
            except Exception as e:
                print(f"❌ Error creating tables: {e}")
            finally:
                conn.close()
    
    def insert_sample_data(self):
        """Insert sample data"""
        conn = self.connect()
        if conn:
            try:
                cur = conn.cursor()
                
                # Insert users
                users = [
                    ('john_doe', 'john@example.com'),
                    ('jane_smith', 'jane@example.com'),
                    ('bob_wilson', 'bob@example.com')
                ]
                
                for user in users:
                    cur.execute(
                        "INSERT INTO users (username, email) VALUES (%s, %s) ON CONFLICT (username) DO NOTHING",
                        user
                    )
                
                # Insert products
                products = [
                    ('Laptop', 999.99, 'High-performance laptop'),
                    ('Mouse', 29.99, 'Wireless mouse'),
                    ('Keyboard', 79.99, 'Mechanical keyboard')
                ]
                
                for product in products:
                    cur.execute(
                        "INSERT INTO products (name, price, description) VALUES (%s, %s, %s)",
                        product
                    )
                
                conn.commit()
                cur.close()
                print("✅ Sample data inserted successfully!")
                
            except Exception as e:
                print(f"❌ Error inserting data: {e}")
            finally:
                conn.close()
    
    def get_users(self):
        """Get all users"""
        conn = self.connect()
        if conn:
            try:
                cur = conn.cursor()
                cur.execute("SELECT * FROM users ORDER BY id")
                users = cur.fetchall()
                cur.close()
                return users
            except Exception as e:
                print(f"❌ Error getting users: {e}")
                return []
            finally:
                conn.close()
        return []
    
    def get_products(self):
        """Get all products"""
        conn = self.connect()
        if conn:
            try:
                cur = conn.cursor()
                cur.execute("SELECT * FROM products ORDER BY id")
                products = cur.fetchall()
                cur.close()
                return products
            except Exception as e:
                print(f"❌ Error getting products: {e}")
                return []
            finally:
                conn.close()
        return []
    
    def add_user(self, username, email):
        """Add new user"""
        conn = self.connect()
        if conn:
            try:
                cur = conn.cursor()
                cur.execute(
                    "INSERT INTO users (username, email) VALUES (%s, %s)",
                    (username, email)
                )
                conn.commit()
                cur.close()
                return True
            except Exception as e:
                print(f"❌ Error adding user: {e}")
                return False
            finally:
                conn.close()
        return False
    
    def add_product(self, name, price, description):
        """Add new product"""
        conn = self.connect()
        if conn:
            try:
                cur = conn.cursor()
                cur.execute(
                    "INSERT INTO products (name, price, description) VALUES (%s, %s, %s)",
                    (name, price, description)
                )
                conn.commit()
                cur.close()
                return True
            except Exception as e:
                print(f"❌ Error adding product: {e}")
                return False
            finally:
                conn.close()
        return False

def setup_database():
    """Initialize the database"""
    db = Database()
    db.create_tables()
    db.insert_sample_data()

if __name__ == "__main__":
    setup_database()