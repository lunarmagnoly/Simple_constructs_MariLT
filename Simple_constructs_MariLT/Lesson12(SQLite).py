from sqlite3 import connect, Error

def create_connection(path):
    connection = None
    try:
        connection = connect(path)
        print("Ühendus on edukalt tehtud")
    except Error as e:
        print(f"Tekkis viga: '{e}'")
    
    return connection

conn = create_connection(r"C:\Users\maril\source\repos\Simple_constructs_MariLT\Simple_constructs_MariLT\AppData\data.db")

def execute_query(connection, query):
    """Execute a write operation (e.g., CREATE, INSERT)"""
    if connection is None:
        print("Ühendust pole loodud!")
        return
    
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Päring on edukalt täidetud!")
    except Error as e:
        print(f"Viga '{e}' päringu täitmisel")

create_users_table = """
 CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    gender TEXT,
    nationality TEXT
);
"""
execute_query(conn, create_users_table)

create_users = """
INSERT INTO users (name, age, gender, nationality)
VALUES
    ('Mati', 25, 'mees', 'USA'),
    ('Lidia', 32, 'naine', 'France'),
    ('Brigitte', 35, 'naine', 'England'),
    ('Mike', 40, 'mees', 'Denmark'),
    ('Elizabeth', 21, 'naine', 'Eesti');
"""
execute_query(conn, create_users)

def execute_read_query(connection, query):
    """Execute a read operation (e.g., SELECT)"""
    if connection is None:
        print("Ühendust pole loodud!")
        return None
    
    cursor = connection.cursor()
    try:
        cursor.execute(query)  # 🔹 FIXED: Now executing the query
        return cursor.fetchall()
    except Error as e:
        print(f"Viga '{e}' päringu täitmisel")
        return None

select_users = "SELECT * FROM users"

users = execute_read_query(conn, select_users)
if users:  # Check if `users` is not None before iterating
    for user in users:
        print(user)

# Close the connection when done
if conn:
    conn.close()

def add_users_query(connection, user_data):
    query="INSERT INTO users(name, age, gender, nationality) VALUES ("+user_data+")"
    execute_query(connection, query)

    insert_user="'"+input("Nimi: ")+"','"+input("Vanus: ")
    +"','"+input("Sugu: ")+"','"+input("Riik: ")+"'"

    add_users_query(conn, insert_user)

def delete_data_from_table(connection, query):
    try:
        cursor=connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Andmed on kustutatud")
    
    except Error as e:
        print(f"Viga '{e}'ndmete kustutamisega")

# print("Andmete kustutame tabelist 'users'")
# delete_data_from_users

