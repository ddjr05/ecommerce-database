-- Schema Creation
CREATE TABLE Customer (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);

CREATE TABLE Staff (
    staff_id INT PRIMARY KEY,
    name VARCHAR(100),
    role VARCHAR(50)
);

CREATE TABLE Product (
    product_id INT PRIMARY KEY,
    name VARCHAR(100),
    price DECIMAL(10,2),
    stock_quantity INT
);

CREATE TABLE Purchase (
    purchase_id INT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    staff_id INT,
    quantity INT,
    purchase_date DATE,
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id),
    FOREIGN KEY (product_id) REFERENCES Product(product_id),
    FOREIGN KEY (staff_id) REFERENCES Staff(staff_id)
);

-- Sample Data
INSERT INTO Customer (customer_id, name, email) VALUES
(1, 'Alice Johnson', 'alice@email.com'),
(2, 'Bob Smith', 'bob@email.com'),
(3, 'Carla Reyes', 'carla@email.com');

INSERT INTO Staff (staff_id, name, role) VALUES
(1, 'David Kim', 'Manager'),
(2, 'Ella Brooks', 'Inventory Clerk');

INSERT INTO Product (product_id, name, price, stock_quantity) VALUES
(1, 'Wireless Mouse', 25.99, 50),
(2, 'Mechanical Keyboard', 89.99, 30),
(3, 'USB-C Hub', 45.50, 20),
(4, 'Laptop Stand', 39.99, 15);

INSERT INTO Purchase (purchase_id, customer_id, product_id, staff_id, quantity, purchase_date) VALUES
(1, 1, 2, 1, 1, '2026-07-10'),
(2, 2, 1, 2, 2, '2026-07-12'),
(3, 3, 3, 1, 1, '2026-07-15'),
(4, 1, 4, 2, 1, '2026-07-20');