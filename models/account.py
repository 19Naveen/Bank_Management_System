from dataclasses import dataclass

@dataclass
class Account:
    account_number: int
    customer_id: int
    balance: float
    account_type: str

    def __str__(self):
        return f"Account Number: {self.account_number}, Balance: {self.balance}, Account Type: {self.account_type}"