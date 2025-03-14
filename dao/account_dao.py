from database import Database

class AccountDao:
    def __init__(self, db: Database):
        self.db = db

    def get_user_accounts(self, user_id: int) -> list:
        query = "SELECT A.account_number, A.account_type, A.balance FROM accounts A JOIN users U JOIN CUSTOMERS C ON A.customer_id = C.customer_id AND C.user_id = U.user_id WHERE U.user_id = %s;"
        result = self.db.execute_fetchall(query, (user_id,))
        return result
    
    def get_accounts(self, account_id: int) -> tuple:
        query = "SELECT A.account_number, A.customer_id, A.balance, A.account_type FROM accounts A JOIN users U JOIN CUSTOMERS C ON A.customer_id = C.customer_id AND C.user_id = U.user_id WHERE A.account_number = %s;"
        result = self.db.execute_fetchone(query, (account_id,))
        return result
    
    def deposit(self, amount: float, account_id: int) -> bool:
        query = "UPDATE accounts SET balance = balance + %s WHERE account_number = %s;"
        self.db.execute(query, (amount, account_id))
        return True
    
    def withdraw(self, amount: float, account_id: int) -> bool:
        query = "UPDATE accounts SET balance = balance - %s WHERE account_number = %s;"
        self.db.execute(query, (amount, account_id))
        return True
    
    def get_balance(self, account_id: int) -> float:
        query = "SELECT balance FROM accounts WHERE account_number = %s;"
        result = self.db.execute_fetchone(query, (account_id,))
        return result[0]
    
    def create_transaction(self, account_id: int, transaction_type: str, amount: float, transaction_date: str, reference_account: int = None) -> bool:
        query = "INSERT INTO transactions (account_number, transaction_type, amount, transaction_date, reference_account) VALUES (%s, %s, %s, %s, %s);"
        self.db.execute(query, (account_id, transaction_type, amount, transaction_date, reference_account))
        return True
    
    def get_transactions(self, account_id: int) -> list:
        query = "SELECT * FROM transactions WHERE account_number = %s ORDER BY transaction_date;"
        result = self.db.execute_fetchall(query, (account_id,))
        return result
    
    def create_account(self, customer_id: int, account_type: str) -> bool:
        query = "INSERT INTO accounts (customer_id, account_type) VALUES (%s, %s);"
        self.db.execute(query, (customer_id, account_type))
        return True
        
    def delete_account(self, account_id: int) -> bool:
        query = "DELETE FROM accounts WHERE account_number = %s;"
        self.db.execute(query, (account_id,))
        return True