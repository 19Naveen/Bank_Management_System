from database import Database 
from view.display import Display
from dao.account_dao import AccountDao
from dao.customer_dao import CustomerDao
from dao.employee_dao import EmployeeDao
from view.CustomerView import CustomerView
from view.EmployeeView import EmployeeView
from service.session_state import SessionState
from controller.customer_controller import CustomerController
from controller.account_controller import AccountController
from controller.employee_controller import EmployeeController

# Session State
session_state = SessionState()

# Initialize the Required class
view = Display()
db = Database()
cust_dao = CustomerDao(db)
account_dao = AccountDao(db)
customer_controller = CustomerController(cust_dao, session_state)
account_controller = AccountController(account_dao, session_state)
customerview = CustomerView(session_state, customer_controller, account_controller)

emp_dao = EmployeeDao(db)
employee_controller = EmployeeController(emp_dao, session_state)
customer_controller = CustomerController(cust_dao, session_state)
account_controller = AccountController(account_dao, session_state)
employeeview = EmployeeView(session_state, employee_controller, account_controller, customer_controller)

db.create_connection()

try:
    running = True
    def stop_loop():
        global running
        running = False

    while running:
        actions = {
            '1': customerview.main,
            '2': employeeview.main,
            '3': stop_loop
        }
        view.main_menu()
        choice = input("Enter your choice: ").strip()

        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid choice, please try again.")
finally:
    db.close_connection()  