import sqlite3
import hashlib


class BankApp:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS accounts (
                id INTEGER PRIMARY KEY,
                username TEXT,
                password TEXT,
                balance REAL
            )
        ''')
        self.conn.commit()

    def create_account(self, username, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        self.cursor.execute("INSERT INTO accounts (username, password, balance) VALUES (?, ?, ?)",
                            (username, hashed_password, 0.0))
        self.conn.commit()

    def login(self, username, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        self.cursor.execute("SELECT * FROM accounts WHERE username=? AND password=?", (username, hashed_password))
        account = self.cursor.fetchone()
        return account

    def check_balance(self, username):
        self.cursor.execute("SELECT balance FROM accounts WHERE username=?", (username,))
        balance = self.cursor.fetchone()
        return balance[0]

    def deposit(self, username, amount):
        current_balance = self.check_balance(username)
        new_balance = current_balance + amount
        self.cursor.execute("UPDATE accounts SET balance=? WHERE username=?", (new_balance, username))
        self.conn.commit()

    def withdraw(self, username, amount):
        current_balance = self.check_balance(username)
        if amount > current_balance:
            return "Insufficient balance"
        new_balance = current_balance - amount
        self.cursor.execute("UPDATE accounts SET balance=? WHERE username=?", (new_balance, username))
        self.conn.commit()

    def transfer(self, sender_username, receiver_username, amount):
        sender_balance = self.check_balance(sender_username)
        if amount > sender_balance:
            return "Insufficient balance"

        receiver_balance = self.check_balance(receiver_username)

        new_sender_balance = sender_balance - amount
        new_receiver_balance = receiver_balance + amount

        self.cursor.execute("UPDATE accounts SET balance=? WHERE username=?", (new_sender_balance, sender_username))
        self.cursor.execute("UPDATE accounts SET balance=? WHERE username=?", (new_receiver_balance, receiver_username))
        self.conn.commit()

    def close(self):
        self.conn.close()


def main():
    bank_app = BankApp("bank.db")

    while True:
        print("\nBank Application.md")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Select an operation: ")

        if choice == "1":
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            bank_app.create_account(username, password)
            print("Account created successfully.")

        elif choice == "2":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            account = bank_app.login(username, password)
            if account:
                print("Login successful.")
                while True:
                    print("\nAccount Menu")
                    print("1. Check Balance")
                    print("2. Deposit")
                    print("3. Withdraw")
                    print("4. Transfer")
                    print("5. Logout")

                    account_choice = input("Select an operation: ")

                    if account_choice == "1":
                        balance = bank_app.check_balance(username)
                        print(f"Balance: ${balance:.2f}")

                    elif account_choice == "2":
                        amount = float(input("Enter deposit amount: "))
                        bank_app.deposit(username, amount)
                        print("Deposit successful.")

                    elif account_choice == "3":
                        amount = float(input("Enter withdrawal amount: "))
                        result = bank_app.withdraw(username, amount)
                        if result == "Insufficient balance":
                            print("Insufficient balance.")
                        else:
                            print("Withdrawal successful.")

                    elif account_choice == "4":
                        receiver_username = input("Enter receiver's username: ")
                        amount = float(input("Enter transfer amount: "))
                        result = bank_app.transfer(username, receiver_username, amount)
                        if result == "Insufficient balance":
                            print("Insufficient balance.")
                        else:
                            print("Transfer successful.")

                    elif account_choice == "5":
                        break
            else:
                print("Login failed. Invalid username or password.")

        elif choice == "3":
            bank_app.close()
            break


if __name__ == "__main__":
    main()
