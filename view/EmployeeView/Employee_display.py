class EmployeeDisplay:
    @staticmethod
    def _display_header(title):
        print("\n" + "-" * 40)
        print(f"  {title}")
        print("-" * 40)

    @staticmethod
    def Menu():
        EmployeeDisplay._display_header('Menu')
        menu = [
            'Employee Details',
            'Create Account',
            'Delete Account',
            'Create Customer',
            'Delete Customer',
            'Assist Customer',
            'Exit'
        ]
        for i, item in enumerate(menu, 1):
            print(f"{i}. {item}")

    @staticmethod
    def assist_customer():
        EmployeeDisplay._display_header("ASSIST CUSTOMER")
        menu = [
            'Customer Account Details',
            'Deposit Money',
            'Withdraw Money',
            'Transfer Money',
            'Exit'
        ]

        for i, item in enumerate(menu, 1):
            print(f"{i}. {item}")


    @staticmethod
    def employee_details(employee):
        EmployeeDisplay._display_header('Employee Details')
        print(f"Employee ID: {employee.employee_id}")
        print(f"Name: {employee.full_name}")
        print(f"Email: {employee.email}")
        print(f"Phone: {employee.phone}")
        print(f"Address: {employee.address}")
        print(f"Role: {employee.position}")
        print(f"Date of Birth: {employee.dob}")

    @staticmethod
    def customer_account_details(account):
        EmployeeDisplay._display_header('Customer Account Details')
        print(f"Account ID: {account.account_number}")
        print(f"Customer ID: {account.customer_id}")
        print(f"Balance: {account.balance}")
        print(f"Type: {account.account_type}")
    
    @staticmethod
    def deposit():
        EmployeeDisplay._display_header("DEPOSIT")

    @staticmethod
    def withdraw():
        EmployeeDisplay._display_header("WITHDRAW")

    @staticmethod
    def transfer():
        EmployeeDisplay._display_header("TRANSFER")

    @staticmethod
    def create_account():
        EmployeeDisplay._display_header("CREATE ACCOUNT")

    @staticmethod
    def delete_account():
        EmployeeDisplay._display_header("DELETE ACCOUNT")

    @staticmethod
    def create_customer():
        EmployeeDisplay._display_header("CREATE CUSTOMER")

    @staticmethod
    def delete_customer():
        EmployeeDisplay._display_header("DELETE CUSTOMER")

    @staticmethod
    def operation_result(operation):
        print(operation, 'Successful')
        print('-'*40)