class Display:
    @staticmethod
    def _display_header(title):
        """Helper method to consistently format headers"""
        print("\n" + "=" * 40)
        print(f"{title:^40}")
        print("=" * 40)

    @staticmethod
    def main_menu():
        Display._display_header("Main Menu")
        print("1. Customer Login")
        print("2. Employee Login")
        print("3. Exit")
        print("-" * 40)

    @staticmethod
    def customer_login():
        Display._display_header("Customer Login")
        print("1. Create Account")
        print("2. Login")
        print("3. Go Back")
        print("-" * 40)

    