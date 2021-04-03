import sqlite3

# global var
db_name = "escalade_specs.db"

def connect_to_db():
   db_conn = sqlite3.connect("escalade_specs.db")
   db_cursor = db_conn.cursor()
   print('Connected to DB')
   return db_conn, db_cursor

def drop_table(db_cursor):
    sql = "drop table if exists escalade_specs"
    db_cursor.execute(sql)
    print("Dropped Table ")

def create_table(db_cursor):
    sql = "create table escalade_specs(VIN text, trim text, price real, mpg real, color_exterior text, color_interior text)"
    db_cursor.execute(sql)
    print("Created Table ")

def select_all(db_cursor):
    sql = "select * from escalade_specs"
    result_set = db_cursor.execute(sql)
    print("\nTable has the following rows: ")
    for row in result_set:
        print(row)
    print()


def insert_row(db_cursor):
    sql = "insert into escalade_specs values (?, ?, ?, ?, ?, ?)"
    vin = input("Enter the VIN (str): ")
    trim = input("Enter the trim (str): ")
    price = float(input("Enter the price (float): "))
    mpg = float(input("Enter the MPG (float): "))
    ext_color = input("Enter the exterior color (str): ")
    int_color= input("Enter the interior color (str): ")
    tuple_of_values = (vin, trim, price, mpg, ext_color, int_color)
    db_cursor.execute(sql,tuple_of_values)
    print("Inserted row into table")
    select_all(db_cursor)

def select_row(db_cursor):
    sql = "Select * from escalade_specs where VIN = ?"
    vin = input("Enter the vin that you want to retrieve: ")
    tuple_of_value = (vin, )
    result_set = db_cursor.execute(sql,tuple_of_value)
    print("\nHere are your results: ")
    for row in result_set:
        print(row)
    print()

def update_row(db_cursor):
    sql = "Update escalade_specs set trim = ?, price = ?, VIN = ?"
    vin = input("Enter the vin that you would like to update: ")
    trim = input("Enter the new value for the trim: ")
    price = float(input("Enter the new value for the price: "))
    tuple_of_values = (trim,price,vin)
    db_cursor.execute(sql, tuple_of_values)
    print("Row updated for vin", vin)

def delete_row(db_cursor):
    sql = "Delete from escalade_specs where VIN = ?"
    vin = input("Enter the vin that you would like to delete: ")
    tuple_of_value = (vin, )
    db_cursor.execute(sql, tuple_of_value)
    print("Row deleted for vin", vin)

def display_menu(db_conn, db_cursor):
    print("Welcome to my database program!")
    while True:
        print("Menu: ")
        print("Enter S to get started and create a new database ")
        print("Enter C to create a new row ")
        print("Enter R to retrieve data ")
        print("Enter U to update a row ")
        print("Enter D to delete a row ")
        print("Enter Q to quit the program ")
        choice = input("Enter your choice ").lower()
        if choice == "s":
            drop_table(db_cursor)
            create_table(db_cursor)
        elif choice == "c":
            insert_row(db_cursor)
        elif choice == "r":
            select_row(db_cursor)
        elif choice == "u":
            update_row(db_cursor)
        elif choice == "d":
            delete_row(db_cursor)
        elif choice == "q":
            print("Goodbye")
            break
        else:
            print("Invalid option entered of", choice)
        db_conn.commit()
        select_all(db_cursor)

def main():
    db_conn, db_cursor = connect_to_db()
    display_menu(db_conn, db_cursor)
    db_conn.close()

main()
