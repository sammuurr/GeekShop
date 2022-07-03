from sqlite3 import Error
from database import DataBase

from config import conn


DataBase.createTables()


def createUser(telegram_id: int, telegram_name: int) -> bool:
    try:
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO users (telegram_id, telegram_name) VALUES (?, ?)",
            (
                telegram_id,
                telegram_name,
            ),
        )

        conn.commit()
        cursor.close()

        return True
    except Error as db_create_error:
        print(f"SQLite: An error has occurred while db was called: {db_create_error}")
        return False


def getUsers(is_admins: bool = True):
    try:
        cursor = conn.cursor()
        if not is_admins:
            cursor.execute("SELECT * FROM users")
            result = cursor.fetchall()
            cursor.close()

            return result
        else:
            cursor.execute("SELECT telegram_id FROM users WHERE access_level == 1")
            result = cursor.fetchall()
            cursor.close()
            admins = []

            for admin in result:
                admins.append(admin[0])

            return admins
    except Error as db_create_error:
        print(f"SQLite: Search Error - {db_create_error}")


def setUserForAdmin(id_, admin: bool = True) -> bool:
    try:
        cursor = conn.cursor()
        if admin:
            cursor.execute(
                f"UPDATE users SET access_level = 1 WHERE id == {id_} OR telegram_id == {id_}"
            )
        else:
            cursor.execute(
                f"UPDATE users SET access_level = 0 WHERE id == {id_} OR telegram_id == {id_}"
            )
        conn.commit()
        cursor.close()

        return True
    except Error as db_create_error:
        print(f"SQLite: Update Error - {db_create_error}")
        return False
