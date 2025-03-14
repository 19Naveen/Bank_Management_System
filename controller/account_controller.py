from dao.account_dao import AccountDao
from models.account import Account
from datetime import datetime       
from service.session_state import SessionState

class AccountController:
    def __init__(self, dao: AccountDao, session_state: SessionState):
        self.account_dao = dao

    def account_details(self, account_id: int):
        res = self.account_dao.get_accounts(account_id)
        if res is None:
            return None
        else:
            return Account(*res)

    def get_user_accounts(self, user_id: int):
        return self.account_dao.get_user_accounts(user_id)

    def deposit(self, account_id: int, amount: float):
        self.account_dao.deposit(amount, account_id)
        self.transaction(account_id, amount, 'deposit')
        return True

    def withdraw(self, account_id: int, amount: float):
        balance = self.account_dao.get_balance(account_id)
        if balance < amount:
            return False
        else:
            self.account_dao.withdraw(amount, account_id)
            self.transaction(account_id, amount, 'withdrawal')
            return True
        

    def transfer(self, account_id: int, amount: float, to_account: int):
        if self.withdraw(account_id, amount):
            self.deposit(to_account, amount)
            self.transaction(account_id, amount, 'withdrawal', to_account)
            self.transaction(to_account, amount, 'transfer', account_id)
            return True
        return False

    def get_balance(self, account_id: int):
        return self.account_dao.get_balance(account_id)

    def transaction(self, account_id: int, amount: float, transaction_type: str, reference_account: int = None):
        if transaction_type == 'transfer':
            self.account_dao.create_transaction(account_id, transaction_type, amount, datetime.now(), reference_account)
        else:
            self.account_dao.create_transaction(account_id, transaction_type, amount, datetime.now())
    

    def view_transactions(self, account_id: int):
        return self.account_dao.get_transactions(account_id)
    

    def create_account(self, customer_id: int, account_type: str):
        return self.account_dao.create_account(customer_id, account_type)
    

    def delete_account(self, account_id: int):
        return self.account_dao.delete_account(account_id)




