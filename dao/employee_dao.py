from database import Database

class EmployeeDao:
    def __init__(self, db: Database):
        self.db = db

    def authenticate(self, email: str, password: str):
        query = "SELECT * FROM users WHERE email = %s AND password = %s"
        values = (email, password)
        result = self.db.execute_fetchone(query, values)
        if result:
            return result
        return False
    
    def get_employee_details(self, user_id: int):
        query = "SELECT * FROM employees WHERE user_id = %s"
        values = (user_id,)
        result = self.db.execute_fetchone(query, values)
        return result