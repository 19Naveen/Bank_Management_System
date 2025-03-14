class SessionState:
    def __init__(self):
        self.current_user = None
        self.current_customer = None
        self.current_account = None

    def set_current_user(self, user):
        self.current_user = user

    def set_current_account(self, account):
        self.current_account = account

    def set_current_customer(self, customer):
        self.current_customer = customer

    def get_current_user(self):
        return self.current_user

    def get_current_account(self):
        return self.current_account

    def get_current_customer(self):
        return self.current_customer