# **Bank Application**

The "Bank Application" is a Python program that simulates basic banking operations. It allows users to create accounts, log in, check balances, deposit and withdraw money, and transfer funds to other accounts. This project is designed to help you practice your Python programming skills, database management, and basic security measures.

### Key Features:

1. **Create Account:** Users can create a new bank account by providing a unique username and password. Passwords are securely hashed using the SHA-256 algorithm before storage.
2. **Login:** Account holders can log in with their usernames and passwords to access their accounts.
3. **Check Balance:** Users can check their account balances.
4. **Deposit:** Account holders can deposit money into their accounts.
5. **Withdraw:** Users can withdraw money from their accounts, provided they have sufficient funds.
6. **Transfer:** Account holders can transfer money to other accounts, ensuring secure fund transfer.

### Project Structure:

- The program uses an SQLite database to store account information, including usernames, hashed passwords, and account balances.
- User passwords are securely hashed using the SHA-256 algorithm before storage to enhance security.
- It includes a `BankApp` class that encapsulates the functionality of the application, making it organized and easy to maintain.

### How to Use:

1. Run the Python program.
2. Select from the available options to create an account, log in, and perform banking operations.

### Why This Project?

This project serves as a practical exercise for intermediate Python programmers. It covers fundamental concepts such as working with databases, user authentication, and class-based application structure. By completing this project, you will improve your Python skills and gain experience in building secure applications.

### Suggested Enhancements:

To further expand and enhance this project, you can consider adding features like:

- User account management: Allow users to change passwords and update account information.
- Transaction history: Keep a record of all transactions for each account.
- Error handling: Implement robust error handling and validation to enhance security.

Feel free to explore and customize this project to suit your learning goals and interests. Happy coding!
