from controller.customer_controller import CustomerController
from controller.employee_controller import EmployeeController

class AuthenticationService:
    def __init__(self, customer_controller: CustomerController = None, employee_controller: EmployeeController = None):
        self.customer_controller = customer_controller  
        self.employee_controller = employee_controller

    def authenticate_customer(self) -> bool:
        """Authenticates customer login."""
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        return self.customer_controller.authenticate(email, password) 
    
    def authenticate_employee(self) -> bool:
        """Authenticates employee login."""
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        return self.employee_controller.authenticate(email, password)  
