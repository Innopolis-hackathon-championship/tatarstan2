import aiosqlite
import asyncio


async def leave_feedback(feedback):
    async with aiosqlite.connect("feedback.sqlite") as con:
        await con.execute("INSERT INTO feedbacks (otziv) VALUES (?)", (feedback,))
        await con.commit()


async def delete_feedback(feedback):
    async with aiosqlite.connect("feedback.sqlite") as con:
        await con.execute(f"DELETE FROM feedbacks WHERE otziv = ?", (feedback,))
        await con.commit()


async def get_feedback():
    async with aiosqlite.connect("feedback.sqlite") as con:
        cursor = await con.execute("SELECT * FROM feedbacks")
        feedbacks = await cursor.fetchall()
        await cursor.close()
        return feedbacks


async def add_info(product_id, bzuk):
    async with aiosqlite.connect("info.sqlite") as con:
        await con.execute("INSERT OR REPLACE INTO infos (product_id, bzuk) VALUES (?, ?)", (product_id, bzuk))
        await con.commit()


async def get_info(product_id) -> list:
    async with aiosqlite.connect("info.sqlite") as con:
        cursor = await con.execute("SELECT bzuk FROM infos WHERE product_id=?", (product_id,))
        res = await cursor.fetchall()
        await cursor.close()
        return res


async def validation(tg_id) -> bool:
    async with aiosqlite.connect("users_db.sqlite") as con:
        cursor = await con.execute("SELECT user_id FROM users")
        result = await cursor.fetchall()
        await cursor.close()
        if (tg_id,) in result:
            return True
        else:
            return False


async def get_menu_buttons() -> dict:
    async with aiosqlite.connect("menu.sqlite") as con:
        cursor = await con.execute("SELECT * FROM products")
        items = await cursor.fetchall()
        await cursor.close()
        res = {}
        for item in items:
            if item[3] > 0:
                res[item[0]] = item[1]
        return res


async def get_menu_numbers() -> dict:
    async with aiosqlite.connect("menu.sqlite") as con:
        cursor = await con.execute("SELECT * FROM products")
        items = await cursor.fetchall()
        await cursor.close()
        res = {}
        for item in items:
            if item[3] > 0:
                res[item[0]] = item[3]
        return res


async def get_balance(tg_id):
    async with aiosqlite.connect("users_db.sqlite") as con:
        cursor = await con.execute(f"SELECT bill FROM users WHERE user_id={tg_id}")
        result = await cursor.fetchone()
        await cursor.close()
        return result


async def get_product_name(id):
    async with aiosqlite.connect("menu.sqlite") as con:
        if id.isdigit():
            cursor = await con.execute(f"SELECT name FROM products WHERE product_id={id}")
            result = await cursor.fetchone()
            await cursor.close()
            return [1, result[0]]
        else:
            return [0, '*аргумент функции "/buy" должен быть целым числом*']


async def get_menu_for_photo():
    async with aiosqlite.connect("menu.sqlite") as con:
        cursor = await con.execute("SELECT * FROM products")
        res = await cursor.fetchall()
        await cursor.close()
        res_1 = []
        for i in res:
            res_1.append([i[0], i[1], i[2], i[3]])
        return res_1


async def add_message(text):
    async with aiosqlite.connect("feedback.sqlite") as con:
        cursor = con.execute('''
            INSERT INTO messages (text)
            VALUES (?)''', (text,))
        con.commit()


async def get_last_10_messages():
    async with aiosqlite.connect("feedback.sqlite") as con:
        con.execute('''
            SELECT text FROM messages
            ORDER BY ROWID DESC
            LIMIT 3
        ''')
        messages = con.fetchall()
        return messages


async def insert_into_korz(name):
    async with aiosqlite.connect("korz.sqlite") as con:
        try:
            cursor = await con.execute(f"SELECT products FROM korzina WHERE user_id ={tg_id}")
            res = await cursor.fetchone()
            res_1 = []
            for i in res:
                res_1.append(i)
            res_1.append(name)
        except:
            await con.execute(f"INSERT OR REPLACE {name} INTO products")
            await con.commit()
            return None
        await con.execute(f"INSERT OR REPLACE {name} INTO products")
        await con.commit()


async def get_korz(tg_id):
    async with aiosqlite.connect("korz.sqlite") as con:
        cursor = await con.execute(f"SELECT products FROM korzina WHERE user_id ={tg_id}")
        res = await cursor.fetchone()
        return ', '.join(res)


async def del_korz(tg_id):
    async with aiosqlite.connect("korz.sqlite") as con:
        cursor = await con.execute(f"delete * FROM korzina WHERE user_id ={tg_id}")
        res = await cursor.fetchone()
        return ', '.join(res[0])

# async def main():
#     result = await get_product_name(2)
#     print(result)
#
#
# asyncio.run(main())
