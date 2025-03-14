from database import Database
from dataclasses import astuple
from models.customers import Customer


class CustomerDao:
    def __init__(self, db: Database):
        self.db = db

    def authenticate(self, email: str, password: str) -> bool:
        self.db.create_connection()
        query = "SELECT * FROM users WHERE email = %s AND password = %s"
        result = self.db.execute_fetchone(query, (email, password))
        return result
    
    def get_customer(self, user_id: int):
        query = "SELECT * FROM customers WHERE user_id = %s"
        result = self.db.execute_fetchone(query, (user_id,))
        return result   

    def create_user(self, email: str, password: str) -> int:
        query = "INSERT INTO users (email, password) VALUES (%s, %s);"
        self.db.execute(query, (email, password))
        return self.db.extract_last_id


    def create_customer(self, customer: Customer) -> int:
        query = "INSERT INTO customers (user_id, full_name, email, phone, address, dob, pan) VALUES (%s, %s, %s, %s, %s, %s, %s);"

        user_id = customer.user_id
        full_name = customer.full_name
        email = customer.email
        phone = customer.phone
        address = customer.address
        dob = customer.dob
        pan = customer.pan

        self.db.execute(query, (user_id, full_name, email, phone, address, dob, pan))
        return self.db.extract_last_id

    def delete_customer(self, cust_id: int):
        query = "DELETE FROM customers WHERE customer_id = %s"
        self.db.execute(query, (cust_id,))
        return True
