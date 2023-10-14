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


async def validation(tg_id):
    async with aiosqlite.connect("users_db.sqlite") as con:
        cursor = await con.execute("SELECT user_id FROM users")
        result = await cursor.fetchall()
        await cursor.close()
        if (tg_id,) in result:
            return 1
        else:
            return 0


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

# async def main():
#     result = await get_balance(846030183)
#     print(result[0])
#
#
#
# asyncio.run(main())
