from dao.customer_dao import CustomerDao
from models.customers import Customer
from service.session_state import SessionState

class CustomerController:
    def __init__(self, dao: CustomerDao, session_state: SessionState):
        self.customer_dao = dao
        self.session_state = session_state

    def authenticate(self, email: str, password: str) -> bool:
        if len(password) < 8:
            return False
        
        user =  self.customer_dao.authenticate(email, password)
        if user:
            self.session_state.set_current_user(user[0])
            return True
        return False
    
    def customer_details(self, user_id: int) -> Customer:
        res = self.customer_dao.get_customer(user_id)
        return Customer(*res)
    
    def create_user(self, email: str, password: str) -> int:
        return self.customer_dao.create_user(email, password)
    
    def create_customer(self, customer: Customer) -> int:
        return self.customer_dao.create_customer(customer)
    
    def delete_customer(self, cust_id: int):
        return self.customer_dao.delete_customer(cust_id)