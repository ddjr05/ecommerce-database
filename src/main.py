import os
import psycopg2

# --- Database connection ---
conn = psycopg2.connect(os.environ["DATABASE_URL"])
cur = conn.cursor()


def view_products():
    cur.execute("SELECT product_id, name, price, stock_quantity FROM Product;")
    rows = cur.fetchall()
    print("\n--- Products ---")
    for row in rows:
        print(f"ID: {row[0]} | Name: {row[1]} | Price: ${row[2]} | Stock: {row[3]}")


def add_product():
    product_id = int(input("Product ID: "))
    name = input("Name: ")
    price = float(input("Price: "))
    stock = int(input("Stock quantity: "))
    cur.execute(
        "INSERT INTO Product (product_id, name, price, stock_quantity) VALUES (%s, %s, %s, %s);",
        (product_id, name, price, stock)
    )
    conn.commit()
    print("Product added.")


def view_customers():
    cur.execute("SELECT customer_id, name, email FROM Customer;")
    rows = cur.fetchall()
    print("\n--- Customers ---")
    for row in rows:
        print(f"ID: {row[0]} | Name: {row[1]} | Email: {row[2]}")


def make_purchase():
    purchase_id = int(input("Purchase ID: "))
    customer_id = int(input("Customer ID: "))
    product_id = int(input("Product ID: "))
    staff_id = int(input("Staff ID: "))
    quantity = int(input("Quantity: "))
    date = input("Purchase date (YYYY-MM-DD): ")
    cur.execute(
        "INSERT INTO Purchase (purchase_id, customer_id, product_id, staff_id, quantity, purchase_date) VALUES (%s, %s, %s, %s, %s, %s);",
        (purchase_id, customer_id, product_id, staff_id, quantity, date)
    )
    conn.commit()
    print("Purchase recorded.")


def view_customer_purchases():
    customer_id = int(input("Customer ID: "))
    cur.execute("""
        SELECT Product.name, Purchase.quantity, Purchase.purchase_date
        FROM Purchase
        JOIN Product ON Purchase.product_id = Product.product_id
        WHERE Purchase.customer_id = %s;
    """, (customer_id,))
    rows = cur.fetchall()
    print(f"\n--- Purchases for Customer {customer_id} ---")
    for row in rows:
        print(f"Product: {row[0]} | Quantity: {row[1]} | Date: {row[2]}")


def main():
    while True:
        print("\n=== E-Commerce CLI ===")
        print("1. View products")
        print("2. Add product")
        print("3. View customers")
        print("4. Make a purchase")
        print("5. View a customer's purchases")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            view_products()
        elif choice == "2":
            add_product()
        elif choice == "3":
            view_customers()
        elif choice == "4":
            make_purchase()
        elif choice == "5":
            view_customer_purchases()
        elif choice == "6":
            cur.close()
            conn.close()
            print("Goodbye.")
            break
        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()