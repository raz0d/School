# FIND TOTAL PAYMENT ACCORDING TO EACH METHOD

USE my_db;

CREATE TABLE payment (
	customer_id INT PRIMARY KEY,
    customer VARCHAR(50) NOT NULL,
    mode VARCHAR(50) NOT NULL,
    city VARCHAR(50) NOT NULL 
);

INSERT INTO payment
	(customer_id, customer, mode, city)
    VALUES
    (101, "Olivia Barrett", "Netbanking", "Poland"),
    (102, "Ethan Sinclair", "Credit Card", "Portland"),
    (103, "Maya Hernandez", "Credit Card", "Seattle"),
    (104, "Liam Donovan", "Netbanking", "Denver"),
    (105, "Sophia Nguyen", "Cr edit Card", "New Orleans"),
    (106, "Caleb Foster", "Debit Card", "Minneapolis"),
    (107, "Ava Patel", "Debit Card", "Phoenix"),
    (108, "Lucas Cartert", "Netbanking", "Boston"),
    (109, "Isabella Martinezt", "Netbanking", "Nashville"),
    (110, "Jackson Brooks", "Credit Card", "Boston");
    
SELECT * FROM payment;

SELECT mode as "Payment Method", 
	count(customer_id) as "Customers using this method"
	FROM payment
    GROUP BY mode
    ORDER BY count(customer_id);