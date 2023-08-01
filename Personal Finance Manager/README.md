# Personal Finance Manager

The Personal Finance Manager is a Python script that helps users manage their personal finances by tracking expenses, setting budgets, and generating spending reports. The script utilizes the Pandas library for data handling and Matplotlib for data visualization.

## Features

1. **Track Expenses:** Allows users to add expenses with details such as date, description, amount, and category.

2. **View Expenses:** Displays a table of all tracked expenses.

3. **Generate Spending Report:** Presents a pie chart visualization of spending based on expense descriptions.

4. **Set Budget:** Enables users to set their monthly budget.

5. **Reset Monthly Budget and Expenses:** Resets the budget and expenses at the beginning of each month.

6. **Check Remaining Budget:** Displays the remaining budget after deducting total expenses from the set budget.

7. **Visualize Expense Distribution:** Shows a bar chart of the total expenses per expense category.

## How to Use

1. Ensure you have Python installed on your machine.

2. Install required libraries using pip:

```bash
   pip install pandas matplotlib
```

3. Run the personal_finance_manager.py script:

```bash
python personal_finance_manager.py
```

4. The script will display the main menu. Here's an example of how you can use the different features of the Personal Finance Manager:

```bash
Personal Finance Manager Menu:
1. Track Expenses
2. View Expenses
3. Generate Spending Report
4. Set Budget
5. Reset Monthly Budget and Expenses
6. Check Remaining Budget
7. Visualize Expense Distribution
8. Exit

Enter your choice (1-8):
```

- Choose option 4 to set your monthly budget:

```bash
Enter your choice (1-8): 4
Enter your budget amount: 1000
Budget set successfully!
```
- Choose option 1 to track expenses:

```bash
Enter your choice (1-8): 1
Enter the date (YYYY-MM-DD): 2023-07-15
Enter the expense description: Groceries
Enter the expense amount: 50.00
Enter the expense category: Food
Expense added successfully!

Enter your choice (1-8): 1
Enter the date (YYYY-MM-DD): 2023-07-16
Enter the expense description: Movie ticket
Enter the expense amount: 20.00
Enter the expense category: Entertainment
Expense added successfully!

Enter your choice (1-8): 1
Enter the date (YYYY-MM-DD): 2023-07-18
Enter the expense description: Gasoline
Enter the expense amount: 40.00
Enter the expense category: Transportation
Expense added successfully!
```

- View the recorded expenses:

```bash
Enter your choice (1-8): 2
        Date      Description  Amount        Category
0  2023-07-15       Groceries    50.0            Food
1  2023-07-16   Movie ticket    20.0   Entertainment
2  2023-07-18       Gasoline    40.0   Transportation
```

- Generate a spending report:

```bash
Enter your choice (1-8): 3
Total Spending: $ 110.0
```

A pie chart will be displayed showing the spending distribution across different expense descriptions.

- Check the remaining budget:

```bash
Enter your choice (1-8): 6
Remaining Budget: $ 890.0
```

- Visualize expense distribution by category:

```bash
  Enter your choice (1-8): 7
```

A bar chart will be displayed showing the total expenses for each expense category.

- You can continue using other options or choose option 8 to exit the Personal Finance Manager.

5. The script stores expenses in the expenses.csv file and the budget in budget.txt file in the same directory as the script.

## Contributing

Contributions to the Personal Finance Manager script are welcome! If you have any suggestions, bug reports, or feature requests, please feel free to open an issue or submit a pull request.   