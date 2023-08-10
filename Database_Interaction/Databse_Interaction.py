import sqlite3


def create_table(connection):
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        position TEXT,
                        salary REAL
                    )''')
    connection.commit()


def insert_data(connection, name, position, salary):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO employees (name, position, salary) VALUES (?, ?, ?)",
                   (name, position, salary))
    connection.commit()


def update_salary(connection, employee_id, new_salary):
    cursor = connection.cursor()
    cursor.execute("UPDATE employees SET salary = ? WHERE id = ?",
                   (new_salary, employee_id))
    connection.commit()


def query_data(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()

    print("\nEmployee Data:")
    for row in rows:
        print(
            f"ID: {row[0]}, Name: {row[1]}, Position: {row[2]}, Salary: {row[3]}")


if __name__ == "__main__":
    database_name = "employee_database.db"

    connection = sqlite3.connect(database_name)
    print(f"Connected to {database_name}")

    create_table(connection)

    insert_data(connection, "John Doe", "Software Engineer", 75000.0)
    insert_data(connection, "Jane Smith", "Data Analyst", 60000.0)

    print("\nAfter Insertions:")
    query_data(connection)

    update_salary(connection, 1, 80000.0)

    print("\nAfter Update:")
    query_data(connection)

    connection.close()
    print(f"Connection to {database_name} closed.")
