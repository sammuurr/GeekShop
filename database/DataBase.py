import sqlite3


def createTables():
    conn = sqlite3.connect("GeekShop.db")

    try:
        cursor = conn.cursor()
        cursor.execute(
            """
        CREATE TABLE "users" (
        "id" INTEGER,
        "telegram_id" INTEGER NOT NULL UNIQUE,
        "telegram_name"	TEXT,
        "access_level" INTEGER DEFAULT 0,
        PRIMARY KEY("id" AUTOINCREMENT)
        );"""
        )

        conn.commit()
        cursor.close()
    except sqlite3.OperationalError:
        print("SQLite: Base uesers is active")
    conn.close()
