import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
conn = sqlite3.connect('homeworkDB.db')
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS homeworks(id INTEGER PRIMARY KEY AUTOINCREMENT,title TEXT,mainText TEXT,creation_date timestamp default current_timestamp );")
cur.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT not null unique, password TEXT not null);")
#cur.execute("select * from users where email = '%s' limit 1" % ('kopnov.nikita@gmail.com'))
print(cur.fetchone())
cur.execute("INSERT INTO users(email, password) VALUES('kopnov.nikita@gmail.com', '%s');" % ("12345678"))
#cur.execute("INSERT INTO homeworks(title, mainText, creation_date) VALUES('10 а дз по литре', 'заполните табличку', '2022-09-12');")

conn.commit()
