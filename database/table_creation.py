import sqlite3


def create_users_db():
    db = sqlite3.connect('users_db.sqlite')
    c = db.cursor()
    c.execute("""CREATE TABLE users (
        user_id integer,
        name text,
        bill integer)""")
    db.commit()
    db.close()


def create_feedback():
    db = sqlite3.connect('feedback.sqlite')
    cursor = db.cursor()
    cursor.execute("""CREATE TABLE feedbacks (
            otziv text)""")
    db.commit()
    db.close()


def create_info():
    db = sqlite3.connect('info.sqlite')
    cursor = db.cursor()
    cursor.execute("""CREATE TABLE infos (
                product_id integer,
                bzuk text)""")  # белки, жиры, углеводы, калорийность
    db.commit()
    db.close()


def create_menu():
    db = sqlite3.connect('menu.sqlite')
    cursor = db.cursor()
    cursor.execute("""CREATE TABLE products (
                    product_id integer,
                    name text,
                    price int,
                    number int)""")
    db.commit()
    db.close()


create_feedback()
