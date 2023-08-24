class Bank:
    def __init__(self):
        self.users = {}
        self.total_balance = 0
        self.total_loan_amount = 0
        self.loan_enabled = True

    def create_account(self, user_name, initial_balance):
        if user_name not in self.users:
            if initial_balance >= 0:
                self.users[user_name] = {
                    'balance': initial_balance,
                    'transaction_history': []
                }
                self.total_balance += initial_balance
                return True
            else:
                print("Initial balance must be non-negative.")
        else:
            print("User already exists.")
        return False

    def deposit(self, user_name, amount):
        if user_name in self.users and amount > 0:
            self.users[user_name]['balance'] += amount
            self.total_balance += amount
            self.users[user_name]['transaction_history'].append(f"Deposited: {amount}")
            return True
        return False

    def withdraw(self, user_name, amount):
        if user_name in self.users and amount > 0:
            if self.users[user_name]['balance'] >= amount:
                self.users[user_name]['balance'] -= amount
                self.total_balance -= amount
                self.users[user_name]['transaction_history'].append(f"Withdrew: {amount}")
                return True
            else:
                print("Insufficient balance.")
        return False

    def transfer(self, sender_name, receiver_name, amount):
        if sender_name in self.users and receiver_name in self.users and amount > 0:
            if self.users[sender_name]['balance'] >= amount:
                self.users[sender_name]['balance'] -= amount
                self.total_balance -= amount
                self.users[receiver_name]['balance'] += amount
                self.users[sender_name]['transaction_history'].append(f"Transferred: {amount} to {receiver_name}")
                self.users[receiver_name]['transaction_history'].append(f"Received: {amount} from {sender_name}")
                return True
            else:
                print("Insufficient balance.")
        return False

    def check_balance(self, user_name):
        if user_name in self.users:
            return self.users[user_name]['balance']
        return None

    def transaction_history(self, user_name):
        if user_name in self.users:
            return self.users[user_name]['transaction_history']
        return None

    def take_loan(self, user_name):
        if user_name in self.users and self.loan_enabled:
            total_amount = 2 * self.users[user_name]['balance']
            self.users[user_name]['balance'] += total_amount
            self.total_loan_amount += total_amount
            self.users[user_name]['transaction_history'].append(f"Took a loan: {total_amount}")
            return total_amount
        return None

class Admin:
    def __init__(self, bank):
        self.bank = bank

    def check_total_balance(self):
        return self.bank.total_balance

    def check_total_loan_amount(self):
        return self.bank.total_loan_amount

    def toggle_loan_feature(self):
        self.bank.loan_enabled = not self.bank.loan_enabled
        return self.bank.loan_enabled

if __name__ == "__main__":
    bank = Bank()
    admin = Admin(bank)

    
    bank.create_account("Akash", 1000)
    bank.create_account("Monir", 500)

   
    bank.deposit("Akash", 300)
    bank.withdraw("Monir", 200)
    bank.transfer("Akash", "Monir", 100)

    print("Akash's balance:", bank.check_balance("Akash"))
    print("Monir's balance:", bank.check_balance("Monir"))

   
    bank.take_loan("Akash")
    print("Akash's balance after taking a loan:", bank.check_balance("Akash"))

    # Admin operations
    print("Total bank balance:", admin.check_total_balance())
    print("Total loan amount:", admin.check_total_loan_amount())

    # Toggle loan feature
    print("Loan feature enabled:", admin.toggle_loan_feature())

