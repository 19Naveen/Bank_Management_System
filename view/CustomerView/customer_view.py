from controller.customer_controller import CustomerController
from controller.account_controller import AccountController
from view.CustomerView.Customer_display import CustomerDisplay
from service.session_state import SessionState
from service.authenticate import AuthenticationService

class CustomerView:
    def __init__(self, session_state: SessionState, cust_controller: CustomerController, acc_controller: AccountController):
        self.account = acc_controller
        self.customer = cust_controller
        self.session_state = session_state

    def main(self):
        auth_service = AuthenticationService(customer_controller=self.customer)
        auth = auth_service.authenticate_customer()
        if auth:
            CustomerDisplay.login_result('Successful')
            self.select_account()
            while True:
                CustomerDisplay.customer_menu()
                choice = input("Enter your choice: ")
                if choice == '1':
                    details = self.customer.customer_details(self.session_state.get_current_user())
                    CustomerDisplay.customer_details(details)

                elif choice == '2':
                    details = self.account.account_details(self.session_state.get_current_account())
                    CustomerDisplay.account_details(details)

                elif choice == '3':
                    CustomerDisplay.deposit()
                    amount = int(input("Enter the amount to deposit: "))
                    self.account.deposit(self.session_state.get_current_account(), amount)
                    CustomerDisplay.operation_result('Deposit')

                elif choice == '4':
                    CustomerDisplay.withdraw()
                    amount = int(input("Enter the amount to withdraw: "))
                    self.account.withdraw(self.session_state.get_current_account(), amount)
                    CustomerDisplay.operation_result('Withdrawal')

                elif choice == '5':
                    CustomerDisplay.transfer()
                    amount = int(input("Enter the amount to Transfer: "))
                    to_account = int(input("Enter the account number to transfer to: "))
                    if self.account.transfer(self.session_state.get_current_account(), amount, to_account):
                        print("Transfer successful.")
                    else:
                        print("Transfer Failed.")
                elif choice == '6':
                    transaction = self.account.view_transactions(self.session_state.get_current_account())
                    CustomerDisplay.view_transactions(transaction)

                elif choice == '7':
                    break
                else:
                    print("Invalid choice. Please try again.")
        else:
            print("Invalid email or password. Please try again.")
            

    def select_account(self):
        while True:
            accounts = self.account.get_user_accounts(self.session_state.get_current_user())
            CustomerDisplay.select_account(accounts)
            account_id = int(input("Enter your account number: "))
            if account_id in [accounts[i][0] for i in range(len(accounts))]:
                self.session_state.set_current_account(account_id)
                break
            else:
                print("Invalid account number. Please try again.")
                CustomerDisplay.login_result('Unsuccessful....')
    