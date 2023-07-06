# Importing the module
import sqlite3

# Writing the Query for creating the exercise table
Create_exercise_table = """
                CREATE TABLE IF NOT EXISTS exercise
                (
                    id INTEGER PRIMARY KEY,
                    date TEXT,
                    data TEXT
                );
        """

# Writing the query for inserting values into exercise table
insert_exercise = """
                INSERT INTO exercise (date, data) VALUES (?, ?);
"""

# Writing the query for inserting values into food table
insert_food = """
                INSERT INTO food (date, data) VALUES (?, ?);
"""

# Writing the query for creating the food table
Create_food_table = """
                CREATE TABLE IF NOT EXISTS food
                (
                    id INTEGER PRIMARY KEY,
                    date TEXT,
                    data TEXT
                );
        """

# Writing the query for deleting the exercise table
delete_exercise_table = """
                    DROP TABLE exercise
        """

# Writing the query for deleting the food table
delete_food_table = """
                    DROP TABLE food
        """

# defining functions for different queries


def connect():
    connection = sqlite3.connect("data.db")
    return connection


def create_table1(connection):
    with connection:
        connection.execute(Create_exercise_table)


def create_table2(connection):
    with connection:
        connection.execute(Create_food_table)


def add_exercise(connection, date, data):
    with connection:
        connection.execute(insert_exercise, (date, data))


def add_food(connection, date, data):
    with connection:
        connection.execute(insert_food, (date, data))


def delete_exercise(connection):
    with connection:
        connection.execute(delete_exercise_table)


def delete_food(connection):
    with connection:
        connection.execute(delete_food_table)
