class CustomerDisplay:
    @staticmethod
    def _display_header(title, length=40):
        """Helper method to consistently format headers"""
        print("\n" + "=" * length)
        print(f"{title:^40}")
        print("=" * length)


    @staticmethod
    def customer_menu():
        CustomerDisplay._display_header("CUSTOMER MENU")
        options = [
            "Customer Details",
            "Account Details",
            "Deposit",
            "Withdraw",
            "Transfer",
            "View Transactions",
            "Logout"
        ]
        
        for i, option in enumerate(options, 1):
            print(f"  {i}. {option}")
        print("-" * 40)


    @staticmethod
    def customer_login():
        CustomerDisplay._display_header("CUSTOMER LOGIN")

    @staticmethod
    def login_result(result):
        print('Login ', result)
        print('-'*40)

    @staticmethod
    def select_account(accounts):
        CustomerDisplay._display_header("SELECT ACCOUNT")
        
        if not accounts:
            print("  No accounts found.")
            return
            
        print(f"  {'Account Number':<15} {'Type':<10} {'Balance':<10}")
        print("  " + "-" * 35)
        
        for i, account in enumerate(accounts, 1):
            account_number, account_type, balance = account[0], account[1], account[2]
            print(f"  {account_number:<15} {account_type:<10} ${balance:,.2f}")
        
        print("-" * 40)
        print("  Enter the number of the account to select")


    @staticmethod
    def customer_details(customer):
        CustomerDisplay._display_header("CUSTOMER DETAILS")
        
        if not customer:
            print("  Customer information not available.")
            return
            
        details = [
            ("Customer ID", customer.customer_id),
            ("Full Name", customer.full_name),
            ("Email", customer.email),
            ("Phone", customer.phone),
            ("Address", customer.address),
            ("Date of Birth", customer.dob),
            ("PAN", customer.pan)
        ]
        
        for label, value in details:
            print(f"  {label:<15}: {value}")
        
        print("-" * 40)


    @staticmethod
    def account_details(account):
        CustomerDisplay._display_header("ACCOUNT DETAILS")
        
        if not account:
            print("  Account information not available.")
            return
            
        details = [
            ("Account Number", account.account_number),
            ("Account Type", account.account_type),
            ("Balance", f"${account.balance:,.2f}")
        ]
        
        for label, value in details:
            print(f"  {label:<15}: {value}")
        
        print("-" * 40)


    @staticmethod
    def transaction_result(success, message):
        """Display transaction result"""
        CustomerDisplay._display_header("TRANSACTION RESULT")
        status = "SUCCESS" if success else "FAILED"
        print(f"  Status: {status}")
        print(f"  {message}")
        print("-" * 40)


    @staticmethod
    def deposit():
        CustomerDisplay._display_header("DEPOSIT")

    @staticmethod
    def withdraw():
        CustomerDisplay._display_header("WITHDRAW")

    @staticmethod
    def transfer():
        CustomerDisplay._display_header("TRANSFER")

    @staticmethod
    def operation_result(operation):
        print(operation, 'Successful')
        print('-'*40)

    @staticmethod
    def view_transactions(transactions):
        CustomerDisplay._display_header("VIEW TRANSACTIONS", 70)
        if not transactions:
            print("  No transactions found.")
        else:
            print(f"  {'Transaction ID':<15} {'Type':<10} {'Amount':<10} {'Date':<20} {'Reference':<10}")
            print("  " + "-" * 70)
            for transaction in transactions:
                account_id, transaction_id, transaction_type, amount, transaction_date, reference_account = transaction
                formatted_date = transaction_date.strftime("%Y-%m-%d %H:%M:%S")
                reference_account_display = reference_account if reference_account else "N/A"
                print(f"  {transaction_id:<15} {transaction_type:<10} ${amount:,.2f}    {formatted_date:<20}  {reference_account_display:<10}")

