import sqlite3

with sqlite3.Connection("key-values.sqlite3") as db:
    key = input('Enter your key: ')
    cursor = db.execute("""SELECT * FROM Text
                           WHERE owner='user1' AND key='{}'"""
                        .format(key))
    print(list(cursor))
