SELECT name, price FROM Product WHERE stock_quantity < 25;

SELECT name, role FROM Staff WHERE role = 'Manager';

SELECT Customer.name AS customer_name, Product.name AS product_name, Purchase.quantity
FROM Purchase
JOIN Customer ON Purchase.customer_id = Customer.customer_id
JOIN Product ON Purchase.product_id = Product.product_id
WHERE Product.price > 30;