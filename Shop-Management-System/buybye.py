import pandas as pd
import os
import time
from datetime import datetime

login_time = datetime.now()


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def header():
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
    files = {
        "sales.csv": ["Item", "Qty", "Total"],
        "stock.csv": ["Product", "Qty"],
        "products.csv": ["Product", "Price"],
        "employees.csv": ["Name", "Role"],
        "liabilities.csv": ["Name", "Amount", "Due"],
        "log.csv": ["Login Time", "Logout Time"]
    }

    for f, cols in files.items():
        if not os.path.exists(f):
            pd.DataFrame(columns=cols).to_csv(f, index=False)


def show_list(df, kind):
    if df.empty:
        print("No data found.\n")
        return

    for i, row in df.iterrows():
        if kind == "sales":
            print(f"{i+1}. {row['Item']} | Qty: {row['Qty']} | ₹{row['Total']}")
        elif kind == "stock":
            print(f"{i+1}. {row['Product']} | Qty: {row['Qty']}")
        elif kind == "products":
            print(f"{i+1}. {row['Product']} | ₹{row['Price']}")
        elif kind == "employees":
            print(f"{i+1}. {row['Name']} | {row['Role']}")
        elif kind == "liab":
            print(f"{i+1}. {row['Name']} | ₹{row['Amount']} | Due: {row['Due']}")


def exit_app():
    logout_time = datetime.now()

    log = pd.read_csv("log.csv")
    log.loc[len(log)] = [login_time, logout_time]
    log.to_csv("log.csv", index=False)

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
    clear()
    header()
    df = pd.read_csv("sales.csv")

    print("SALES\n")
    print("1. View")
    print("2. Add")

    choice = input(">> ")

    if choice == "1":
        clear()
        header()
        show_list(df, "sales")
        input("\nEnter...")

    elif choice == "2":
        item = input("Item: ")
        qty = int(input("Qty: "))
        price = float(input("Price (₹): "))
        total = qty * price

        df.loc[len(df)] = [item, qty, total]
        df.to_csv("sales.csv", index=False)

        print(f"Saved: ₹{total}")
        input("Enter...")


def stock_menu():
    clear()
    header()
    df = pd.read_csv("stock.csv")

    print("STOCK\n")
    print("1. View")
    print("2. Add/Update")
    print("3. Search")

    choice = input(">> ")

    if choice == "1":
        clear()
        header()
        show_list(df, "stock")
        input("\nEnter...")

    elif choice == "2":
        name = input("Product: ")
        qty = int(input("Qty: "))

        # use case-insensitive matching to keep behavior consistent with search
        name_lower = name.lower()
        product_match = df["Product"].str.lower() == name_lower

        if product_match.any():
            df.loc[product_match, "Qty"] = qty
        else:
            df.loc[len(df)] = [name, qty]

        df.to_csv("stock.csv", index=False)
        print("Stock updated.")
        input("Enter...")

    elif choice == "3":
        name = input("Search: ")
        clear()
        header()
        result = df[df["Product"].str.contains(name, case=False)]
        show_list(result, "stock")
        input("\nEnter...")


def product_menu():
    clear()
    header()
    df = pd.read_csv("products.csv")

    print("PRODUCTS\n")
    print("1. View")
    print("2. Add")
    print("3. Change Price")

    choice = input(">> ")

    if choice == "1":
        clear()
        header()
        show_list(df, "products")
        input("\nEnter...")

    elif choice == "2":
        name = input("Name: ")
        price = float(input("Price (₹): "))
        df.loc[len(df)] = [name, price]
        df.to_csv("products.csv", index=False)
        print("Product added.")
        input("Enter...")

    elif choice == "3":
        name = input("Product: ")
        price = float(input("New price (₹): "))
        df.loc[df["Product"] == name, "Price"] = price
        df.to_csv("products.csv", index=False)
        print("Price updated.")
        input("Enter...")


def employee_menu():
    clear()
    header()
    df = pd.read_csv("employees.csv")

    print("EMPLOYEES\n")
    print("1. View")
    print("2. Add")
    print("3. Filter")

    choice = input(">> ")

    if choice == "1":
        clear()
        header()
        show_list(df, "employees")
        input("\nEnter...")

    elif choice == "2":
        name = input("Name: ")
        role = input("Role: ")
        df.loc[len(df)] = [name, role]
        df.to_csv("employees.csv", index=False)
        print("Employee added.")
        input("Enter...")

    elif choice == "3":
        role = input("Role: ")
        clear()
        header()
        result = df[df["Role"].str.contains(role, case=False)]
        show_list(result, "employees")
        input("\nEnter...")


def liability_menu():
    clear()
    header()
    df = pd.read_csv("liabilities.csv")

    print("LIABILITIES\n")
    print("1. View")
    print("2. Add")

    choice = input(">> ")

    if choice == "1":
        clear()
        header()
        show_list(df, "liab")
        input("\nEnter...")

    elif choice == "2":
        name = input("Name: ")
        amt = float(input("Amount (₹): "))
        due = input("Due date: ")

        df.loc[len(df)] = [name, amt, due]
        df.to_csv("liabilities.csv", index=False)

        print("Liability added.")
        input("Enter...")


def main():
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