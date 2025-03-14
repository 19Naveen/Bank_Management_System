CREATE DATABASE IF NOT EXISTS bank_db;
USE bank_db;

-- Users Table (Authentication)
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(25) UNIQUE NOT NULL,
    password VARCHAR(20) NOT NULL
);

-- Customers Table (Customer Details)
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(15) UNIQUE NOT NULL,
    address TEXT NOT NULL,
    dob DATE NOT NULL,
    pan BIGINT UNIQUE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- Accounts Table (Bank Accounts)
CREATE TABLE accounts (
    account_number INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    balance DECIMAL(10,2) NOT NULL DEFAULT 0.00,
    account_type ENUM('savings', 'current') NOT NULL DEFAULT 'savings',
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
);

-- TRANSACTION table 
CREATE TABLE transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    account_number INT NOT NULL,
    transaction_type ENUM('deposit', 'withdrawal', 'transfer') NOT NULL,
    amount DECIMAL(10,2) NOT NULL CHECK (amount > 0),
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    reference_account INT NULL,  -- Used for transfers
    FOREIGN KEY (account_number) REFERENCES accounts(account_number) ON DELETE CASCADE,
    FOREIGN KEY (reference_account) REFERENCES accounts(account_number) ON DELETE CASCADE
);


-- Branch table
CREATE TABLE branches (
    branch_id INT AUTO_INCREMENT PRIMARY KEY,
    branch_name VARCHAR(100) NOT NULL,
    branch_code VARCHAR(20) UNIQUE NOT NULL,
    address TEXT NOT NULL,
    phone VARCHAR(15) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    manager_id INT
);

-- Employee table
CREATE TABLE employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(15) UNIQUE NOT NULL,
    address TEXT NOT NULL,
    dob DATE NOT NULL,
    position VARCHAR(50) NOT NULL,
    branch_id INT NOT NULL,
    user_id INT NOT NULL,
    FOREIGN KEY (branch_id) REFERENCES branches(branch_id) ON DELETE RESTRICT,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- -----SAMPLE DATA -------
INSERT INTO USERS(email, password) VALUES('naveen@2004.com', 'naveen1234');
INSERT INTO customers (user_id, full_name, email, phone, address, dob, pan) 
VALUES (1, 'NaveenKumar', 'naveen@2004.com', '+917200458723', '111/1, Ramanathapuram, Coimbatore', '2004-08-19', 720045);
INSERT INTO accounts(customer_id, account_type) VALUES (1, 'savings');

INSERT INTO users (email, password) VALUES ('Nikhil@bank.com', 'wilson123');
INSERT INTO branches (branch_name, branch_code, address, phone, email, manager_id) VALUES 
('Nanjundapuram Branch', 'NJ001', '123 Main Street, Nanjundapuram road, Coimbatore 641036', '555-123-4567', 'nanjundapuram@bank.com', NULL);
INSERT INTO employees (full_name, email, phone, address, dob, position, branch_id, user_id) VALUES 
('Nikhil', 'Nikhil@bank.com', '9820045213', '69/5, Ramanathapuram, Coimbatore', '2004-10-15', 'Branch Manager', 1, 2);
UPDATE branches SET manager_id = 2 WHERE branch_id = 1;