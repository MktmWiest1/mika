import sqlite3
from random import randint

database1 = sqlite3.connect('sever.sqlite4')
sql = database1.cursor()
sql.execute(
    """CREATE TABLE IF NOT EXISTS users (
    login TEXT, 
    password TEXT,
    cash INT
    )
    """
)
database1.commit()


def register_user():
    global user_login, user_passpord, balance
    user_login = input("LOGIN: ")
    user_passpord = input("Password")
    number = randint(1, 2)

    for i in sql.execute(f"SELECT cash FROM users WHERE login= '{user_login}'"):
        balance = i[0]

    sql.execute(f"SELECT login FROM users WHERE login = '{user_login}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO users VALUES (?, ?, ?)", (user_login, user_passpord, 0))
        database1.commit()
        print("User registered")
        for value in sql.execute("SELECT * FROM users"):
            print(value)
    else:
        if number == 1:
            sql.execute(f"UPDATE users SET cash = {120 + balance} WHERE login = '{user_login}'")
            print("You win money")
            database1.commit()

        for value in sql.execute("SELECT * FROM users"):
            print(value)
        else:
            print("You lose")
            for value in sql.execute("SELECT * FROM users"):
                print(value)


def delet_user():
    sql.execute(f"DELET FROM users WHERE login = '{user_login}'")
    database1.commit()
    print('User deleted')


def enter_user():
    print('Welcom to the Fortune!')
    sql.excute('SELECT login, cash FROM users')
    row = sql.fetchall()
    print(row)


if __name__ == "__main__":
    register_user()
