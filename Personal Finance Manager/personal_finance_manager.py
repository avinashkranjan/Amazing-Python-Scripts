import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


def track_expenses():
    date = input("Enter the date (YYYY-MM-DD): ")
    description = input("Enter the expense description: ")
    amount = float(input("Enter the expense amount: "))
    category = input("Enter the expense category: ")

    try:
        df = pd.read_csv("expenses.csv")
    except FileNotFoundError:
        df = pd.DataFrame(
            columns=["Date", "Description", "Amount", "Category"])

    df = df.append({"Date": date, "Description": description,
                   "Amount": amount, "Category": category}, ignore_index=True)
    df.to_csv("expenses.csv", index=False)

    print("Expense added successfully!")


def view_expenses():
    try:
        df = pd.read_csv("expenses.csv")
        print(df)
    except FileNotFoundError:
        print("No expenses found.")


def generate_spending_report():
    try:
        df = pd.read_csv("expenses.csv")
        total_spending = df["Amount"].sum()

        plt.figure(figsize=(8, 6))
        plt.pie(df["Amount"], labels=df["Description"], autopct="%1.1f%%")
        plt.title("Spending Report")
        plt.show()

        print("Total Spending: $", total_spending)
    except FileNotFoundError:
        print("No expenses found.")


def set_budget():
    budget = float(input("Enter your budget amount: "))
    with open("budget.txt", "w") as file:
        file.write(str(budget))
    print("Budget set successfully!")


def reset_monthly_budget():
    now = datetime.now()
    first_day_of_month = now.replace(day=1).strftime("%Y-%m-%d")
    df = pd.DataFrame(columns=["Date", "Description", "Amount", "Category"])
    df.to_csv("expenses.csv", index=False)

    print("Monthly budget and expenses reset successfully.")


def check_budget():
    try:
        with open("budget.txt", "r") as file:
            budget = float(file.read())
        df = pd.read_csv("expenses.csv")
        total_spending = df["Amount"].sum()
        remaining_budget = budget - total_spending
        print("Remaining Budget: $", remaining_budget)
    except FileNotFoundError:
        print("Budget not set. Please set a budget first.")


def visualize_expense_distribution():
    try:
        df = pd.read_csv("expenses.csv")
        category_group = df.groupby("Category")["Amount"].sum()

        plt.figure(figsize=(10, 6))
        plt.bar(category_group.index, category_group.values)
        plt.title("Expense Distribution by Category")
        plt.xlabel("Expense Category")
        plt.ylabel("Total Amount")
        plt.xticks(rotation=45)
        plt.show()
    except FileNotFoundError:
        print("No expenses found.")


def main():
    while True:
        print("\nPersonal Finance Manager Menu:")
        print("1. Track Expenses")
        print("2. View Expenses")
        print("3. Generate Spending Report")
        print("4. Set Budget")
        print("5. Reset Monthly Budget and Expenses")
        print("6. Check Remaining Budget")
        print("7. Visualize Expense Distribution")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            track_expenses()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            generate_spending_report()
        elif choice == "4":
            set_budget()
        elif choice == "5":
            reset_monthly_budget()
        elif choice == "6":
            check_budget()
        elif choice == "7":
            visualize_expense_distribution()
        elif choice == "8":
            print("Exiting the Personal Finance Manager.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
