# Database Project with PostgreSQL

This project demonstrates integration with PostgreSQL database.

## Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Set up PostgreSQL database in pgAdmin 4
3. Configure database connection in `.env` file
4. Run: `python database.py` to create tables
5. Run: `python app.py` to start application

## Database Schema

- `users` table: user_id, username, email, created_at
- `products` table: product_id, name, price, description, created_at