from view.EmployeeView.Employee_display import EmployeeDisplay
from controller.employee_controller import EmployeeController
from controller.account_controller import AccountController
from controller.customer_controller import CustomerController
from service.session_state import SessionState
from service.authenticate import AuthenticationService
from models.customers import Customer


class EmployeeView:
    def __init__(self, session_state: SessionState, employee_controller: EmployeeController, account_controller: AccountController, customer_controller: CustomerController):
        self.session_state = session_state
        self.employee_controller = employee_controller
        self.account_controller = account_controller
        self.customer_controller = customer_controller

    def main(self):
        auth_service = AuthenticationService(employee_controller=self.employee_controller)
        auth = auth_service.authenticate_employee()
        if auth:
            while True:
                EmployeeDisplay.Menu()
                choice = input('Enter choice: ')

                if choice == '1':  
                    emp = self.employee_controller.employee_details()
                    EmployeeDisplay.employee_details(emp)

                elif choice == '2': 
                    EmployeeDisplay.create_account()
                    cust_id = int(input('Enter Customer ID: '))
                    acc_type = input('Enter Account Type [savings/current]: ')
                    self.account_controller.create_account(cust_id, acc_type)
                    EmployeeDisplay.operation_result('Account Creation')

                elif choice == '3':  
                    EmployeeDisplay.delete_account()
                    acc_id = int(input('Enter Account ID: '))
                    self.account_controller.delete_account(acc_id)
                    EmployeeDisplay.operation_result('Account Deletion')

                elif choice == '4':  
                    EmployeeDisplay.create_customer()
                    email = input('Enter your Email:')
                    password = input('Enter your Password:')
                    print(f'Successfully Created Username and Password: {email} and {password}\nEnter other Details:')
                    user_id = self.customer_controller.create_user(email, password)
                    new_customer = self.cust_create_get_input(user_id)
                    cust_id = self.customer_controller.create_customer(new_customer)
                    acc_type = input('Enter Account Type [savings/current]: ')
                    self.account_controller.create_account(cust_id, acc_type)
                    EmployeeDisplay.operation_result('Customer Creation')

                elif choice == '5': 
                    EmployeeDisplay.delete_customer()
                    cust_id = int(input('Enter Customer ID: '))
                    self.customer_controller.delete_customer(cust_id)
                    EmployeeDisplay.operation_result('Account Deletion')

                elif choice == '6': 
                    self.assist_customer()

                elif choice == '7':
                    break

        else:
            print('Invalid Email/Password....')

    def assist_customer(self):
        """Handles assisting a customer with transactions and account details."""
        acc_id = input('Enter Account ID: ')
        self.session_state.set_current_account(acc_id)
        while True:
            EmployeeDisplay.assist_customer()

            sub_choice = input('Enter choice: ')
            if sub_choice == '1':  
                acc = self.account_controller.account_details(self.session_state.current_account)
                EmployeeDisplay.customer_account_details(acc)

            elif sub_choice == '2':  
                EmployeeDisplay.deposit()
                amount = float(input('Enter amount: '))
                self.account_controller.deposit(self.session_state.current_account, amount)
                EmployeeDisplay.operation_result('Deposit')

            elif sub_choice == '3':  
                EmployeeDisplay.withdraw()
                amount = float(input('Enter amount: '))
                self.account_controller.withdraw(self.session_state.current_account, amount)
                EmployeeDisplay.operation_result('Withdrawal')

            elif sub_choice == '4': 
                EmployeeDisplay.transfer()
                amount = float(input('Enter amount: '))
                to_account = int(input('Enter account ID to transfer to: '))
                self.account_controller.transfer(self.session_state.current_account, amount, to_account)
                EmployeeDisplay.operation_result('Transfer')

            elif sub_choice == '5':  
                break

    @staticmethod
    def cust_create_get_input(user_id: int) -> Customer:
        """Gathers customer details and returns a Customer object."""
        full_name = input('Enter Full Name: ')
        email = input('Enter Email: ')
        phone = input('Enter Phone: ')
        address = input('Enter Address: ')
        dob = input('Enter DOB: ')
        pan = input('Enter PAN: ')
        return Customer(customer_id=None, user_id=user_id, full_name=full_name, email=email, phone=phone, address=address, dob=dob, pan=pan)
    
