import sqlite3


def example():
    con = sqlite3.connect("users_db.sqlite")
    cursor = con.cursor()
    cursor.executemany("INSERT INTO users (name, user_id, balance) VALUES (?, ?, ?)",
                       (('petr', 1, 100),))
    cursor.execute("SELECT * FROM users")
    print(cursor.fetchone())
    con.commit()
    con.close()


def leave_feedback(product_id, feedback):
    con = sqlite3.connect("feedback.sqlite")
    con.executemany("INSERT INTO feedbacks (otziv) VALUE (?)",
                    ((product_id, feedback),))
    con.commit()
    con.close()


def delete_feedback(feedback):
    con = sqlite3.connect("feedback.sqlite")
    con.executemany(f"DELETE * FROM feedbacks WHERE otziv = VALUE (?)",
                    (feedback,))
    con.commit()
    con.close()


def get_feedback():
    con = sqlite3.connect("feedback.sqlite")
    con.executemany(f"SELECT * FROM feedbacks")
    con.close()


def add_info(product_id, bzuk):
    con = sqlite3.connect("info.sqlite")
    con.executemany("INSERT OR REPLACE INTO infos (product_id, bzuk) VALUES (?, ?)",
                    ((product_id, bzuk),))
    con.commit()
    con.close()


def get_info(product_id) -> list:
    con = sqlite3.connect("info.sqlite")
    res = con.executemany(f"SELECT bzuk FROM infos WHERE product_id = VALUE (?)", (product_id,)).fetchall()
    con.commit()
    con.close()
    return res


def validation(tg_id) -> bool:
    con = sqlite3.connect("database/users_db.sqlite")
    if (tg_id,) in con.execute(f"SELECT user_id FROM users").fetchall():
        con.close()
        return True
    else:
        con.close()
        return False
