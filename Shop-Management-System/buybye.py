import os
import time
from datetime import datetime

import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
login_time = datetime.now()


def data_path(filename):
    """Return the full path to a data file inside the script directory."""
    return os.path.join(BASE_DIR, filename)


def clear():
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def header():
    """Print the app banner and title."""
    print(r"""
██████╗ ██╗   ██╗██╗   ██╗██████╗ ██╗   ██╗███████╗
██╔══██╗██║   ██║╚██╗ ██╔╝██╔══██╗╚██╗ ██╔╝██╔════╝
██████╔╝██║   ██║ ╚████╔╝ ██████╔╝ ╚████╔╝ █████╗
██╔══██╗██║   ██║  ╚██╔╝  ██╔══██╗  ╚██╔╝  ██╔══╝
██████╔╝╚██████╔╝   ██║   ██████╔╝   ██║   ███████╗
╚═════╝  ╚═════╝    ╚═╝   ╚═════╝    ╚═╝   ╚══════╝
""")
    print("BuyBye\n")


def setup():
    """Create the CSV data files if they do not already exist."""
    files = {
        "sales.csv": ["Item", "Qty", "Total"],
        "stock.csv": ["Product", "Qty"],
        "products.csv": ["Product", "Price"],
        "employees.csv": ["Name", "Role"],
        "liabilities.csv": ["Name", "Amount", "Due"],
        "log.csv": ["Login Time", "Logout Time"],
    }

    for filename, cols in files.items():
        path = data_path(filename)
        if not os.path.exists(path):
            pd.DataFrame(columns=cols).to_csv(path, index=False)


def show_list(df, kind):
    """Display rows from a dataframe based on the selected section."""
    if df.empty:
        print("No data found.\n")
        return

    for i, row in df.iterrows():
        if kind == "sales":
            print(f"{i + 1}. {row['Item']} | Qty: {row['Qty']} | ₹{row['Total']}")
        elif kind == "stock":
            print(f"{i + 1}. {row['Product']} | Qty: {row['Qty']}")
        elif kind == "products":
            print(f"{i + 1}. {row['Product']} | ₹{row['Price']}")
        elif kind == "employees":
            print(f"{i + 1}. {row['Name']} | {row['Role']}")
        elif kind == "liab":
            print(f"{i + 1}. {row['Name']} | ₹{row['Amount']} | Due: {row['Due']}")


def pause(message="\nEnter..."):
    """Pause execution until the user presses Enter."""
    input(message)


def prompt_text(prompt):
    """Prompt the user for a non-empty text value."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Please enter a value.")


def prompt_int(prompt):
    """Prompt the user for a whole number value."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid whole number.")


def prompt_float(prompt):
    """Prompt the user for a numeric value."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def show_menu(title, options):
    """Display a menu and return the user's selection."""
    clear()
    header()
    print(f"{title}\n")
    for option in options:
        print(option)
    return input(">> ")


def exit_app():
    """Log the session end time and show the logout animation."""
    logout_time = datetime.now()
    log_path = data_path("log.csv")

    log = pd.read_csv(log_path)
    log.loc[len(log)] = [login_time, logout_time]
    log.to_csv(log_path, index=False)

    clear()
    header()

    for i in range(3):
        print("Logging out" + "." * (i + 1))
        time.sleep(0.5)
        clear()
        header()

    print("\nSession saved ✔")
    print("Bye 👋\n")
    time.sleep(1)


def sales_menu():
    """Manage sales entries through the sales menu."""
    df = pd.read_csv(data_path("sales.csv"))
    choice = show_menu("SALES", ["1. View", "2. Add"])

    if choice == "1":
        clear()
        header()
        show_list(df, "sales")
        pause()

    elif choice == "2":
        item = prompt_text("Item: ")
        qty = prompt_int("Qty: ")
        price = prompt_float("Price (₹): ")
        total = qty * price

        df.loc[len(df)] = [item, qty, total]
        df.to_csv(data_path("sales.csv"), index=False)

        print(f"Saved: ₹{total}")
        pause()


def stock_menu():
    """Manage stock entries through the stock menu."""
    df = pd.read_csv(data_path("stock.csv"))
    choice = show_menu("STOCK", ["1. View", "2. Add/Update", "3. Search"])

    if choice == "1":
        clear()
        header()
        show_list(df, "stock")
        pause()

    elif choice == "2":
        name = prompt_text("Product: ")
        qty = prompt_int("Qty: ")

        # use case-insensitive matching to keep behavior consistent with search
        name_lower = name.lower()
        product_match = df["Product"].astype(str).str.lower() == name_lower

        if product_match.any():
            df.loc[product_match, "Qty"] = qty
        else:
            df.loc[len(df)] = [name, qty]

        df.to_csv(data_path("stock.csv"), index=False)
        print("Stock updated.")
        pause()

    elif choice == "3":
        name = prompt_text("Search: ")
        clear()
        header()
        result = df[df["Product"].str.contains(name, case=False)]
        show_list(result, "stock")
        pause()


def product_menu():
    """Manage product records through the products menu."""
    df = pd.read_csv(data_path("products.csv"))
    choice = show_menu("PRODUCTS", ["1. View", "2. Add", "3. Change Price"])

    if choice == "1":
        clear()
        header()
        show_list(df, "products")
        pause()

    elif choice == "2":
        name = prompt_text("Name: ")
        price = prompt_float("Price (₹): ")
        df.loc[len(df)] = [name, price]
        df.to_csv(data_path("products.csv"), index=False)
        print("Product added.")
        pause()

    elif choice == "3":
        name = prompt_text("Product: ")
        price = prompt_float("New price (₹): ")
        df.loc[df["Product"] == name, "Price"] = price
        df.to_csv(data_path("products.csv"), index=False)
        print("Price updated.")
        pause()


def employee_menu():
    """Manage employee records through the employees menu."""
    df = pd.read_csv(data_path("employees.csv"))
    choice = show_menu("EMPLOYEES", ["1. View", "2. Add", "3. Filter"])

    if choice == "1":
        clear()
        header()
        show_list(df, "employees")
        pause()

    elif choice == "2":
        name = prompt_text("Name: ")
        role = prompt_text("Role: ")
        df.loc[len(df)] = [name, role]
        df.to_csv(data_path("employees.csv"), index=False)
        print("Employee added.")
        pause()

    elif choice == "3":
        role = prompt_text("Role: ")
        clear()
        header()
        result = df[df["Role"].str.contains(role, case=False)]
        show_list(result, "employees")
        pause()


def liability_menu():
    """Manage liabilities through the liabilities menu."""
    df = pd.read_csv(data_path("liabilities.csv"))
    choice = show_menu("LIABILITIES", ["1. View", "2. Add"])

    if choice == "1":
        clear()
        header()
        show_list(df, "liab")
        pause()

    elif choice == "2":
        name = prompt_text("Name: ")
        amt = prompt_float("Amount (₹): ")
        due = prompt_text("Due date: ")

        df.loc[len(df)] = [name, amt, due]
        df.to_csv(data_path("liabilities.csv"), index=False)

        print("Liability added.")
        pause()


def main():
    """Run the main interactive shop management loop."""
    while True:
        clear()
        header()

        print("1. Sales")
        print("2. Stock")
        print("3. Products")
        print("4. Employees")
        print("5. Liabilities")
        print("0. Exit")

        choice = input(">> ")

        if choice == "1":
            sales_menu()
        elif choice == "2":
            stock_menu()
        elif choice == "3":
            product_menu()
        elif choice == "4":
            employee_menu()
        elif choice == "5":
            liability_menu()
        elif choice == "0":
            exit_app()
            break


if __name__ == "__main__":
    setup()
    main()
    