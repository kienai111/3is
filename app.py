from database import Database

def main():
    db = Database()
    
    print("🚀 Database Application")
    
    while True:
        print("\n1. View users")
        print("2. Add user")
        print("3. View products")
        print("4. Add product")
        print("5. Exit")
        
        choice = input("\nChoose option: ").strip()
        
        if choice == '1':
            view_users(db)
        elif choice == '2':
            add_user(db)
        elif choice == '3':
            view_products(db)
        elif choice == '4':
            add_product(db)
        elif choice == '5':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option!")

def view_users(db):
    """View all users"""
    users = db.get_users()
    
    if not users:
        print("\nNo users found.")
        return
    
    print("\n--- Users ---")
    for user in users:
        print(f"ID: {user[0]}, Username: {user[1]}, Email: {user[2]}, Created: {user[3]}")

def add_user(db):
    """Add new user"""
    print("\n➕ Add New User")
    username = input("Username: ")
    email = input("Email: ")
    
    if db.add_user(username, email):
        print("✅ User added successfully!")
    else:
        print("❌ Failed to add user. Username might already exist.")

def view_products(db):
    """View all products"""
    products = db.get_products()
    
    if not products:
        print("\nNo products found.")
        return
    
    print("\n--- Products ---")
    for product in products:
        print(f"ID: {product[0]}, Name: {product[1]}, Price: ${product[2]}, Description: {product[3]}")

def add_product(db):
    """Add new product"""
    print("\n➕ Add New Product")
    name = input("Name: ")
    price = input("Price: ")
    description = input("Description: ")
    
    try:
        price = float(price)
        if db.add_product(name, price, description):
            print("✅ Product added successfully!")
        else:
            print("❌ Failed to add product.")
    except ValueError:
        print("❌ Invalid price format. Please enter a number.")

if __name__ == "__main__":
    main()