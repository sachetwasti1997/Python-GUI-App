import sqlite3

conn = sqlite3.connect("books.db")


def droptable():
    conn.execute("DROP TABLE IF EXISTS records")

def connect():
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS records(id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    cur.close()


def closeConnection():
    conn.close()

def insert(title, author, year, isbn):
    cur = conn.cursor()
    cur.execute("INSERT INTO records VALUES(NULL, ?, ?, ?, ?)",(title, author, year, isbn))
    cur.connection.commit()
    cur.close()

def view():
    cur = conn.cursor()
    cur.execute("SELECT * FROM records")
    resuts = cur.fetchall()
    cur.close()
    return resuts

def search(title="", author="", year="", isbn="", id=""):
    cur=conn.cursor()
    if id!="": id = int(id)
    cur.execute("SELECT * FROM records WHERE title=? OR author=? OR year=? OR isbn=? OR id=?",(title, author, year, isbn, id))
    result = cur.fetchall()
    cur.close()
    return result

def delete(id):
    cur = conn.cursor()
    cur.execute("DELETE FROM records WHERE id=?",(id,))
    cur.connection.commit()
    cur.close()

def update(id, title, author, year, isbn):
    cur = conn.cursor()
    # if year != "": year= int(year)
    # if isbn!= "": isbn=int(isbn)
    # id = int(id)
    cur.execute("UPDATE records SET title=?, author=?, year=?,  isbn=? WHERE id=?",(title, author, year, isbn, id))
    cur.connection.commit()
    cur.close()

if __name__ == '__main__':
    connect()
    # closeConnection()
    # delete(4)
    # insert("The Man", "Sam Smith", 1997, 445687543)
    # insert("The Volatile Reality", "Joe Writer", 1912, 34618972)
    # insert("The Evil", "Sundar Sam", 2000, 56240217)
    # insert("Sunrise", "Books Read Inc.", 1900, 2135682)
    # insert("Igniion", "Jhon Tiger", 1922, 3389492)
    # insert("FuckBoy", "Tailor", 1888, 2367902)
    # insert("Someone Invisible", "Jhonathan Merchant", 1800, 215788567)

    # print(view())
    # print(search(isbn=str(231231444)))
    # delete(5)
    # delete(7)
    # print(view())
    # update(5, title='Ignition')
    for row in view():
        print(row)
    # print(view())
    # droptable()