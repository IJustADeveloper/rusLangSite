import sqlite3


def get_data(n):
    conn = sqlite3.connect('homeworkDB.db')
    cur = conn.cursor()
    n -= 1
    cur.execute("select * from homeworks  order by creation_date desc limit 10*%s" % n)
    hw_id = cur.fetchall()
    print(hw_id)
    if len(hw_id)>0:
        cur.execute("select * from homeworks where id<%s order by creation_date desc limit 10" % hw_id[len(hw_id)-1][0])
    else:
        cur.execute("select * from homeworks order by creation_date desc limit 10")
    conn.commit()
    a = cur.fetchall()
    return a, len(cur.execute("select * from homeworks where id < %s order by creation_date desc " % a[len(a)-1][0]).fetchall())>0


def add_data(t, mt):
    conn = sqlite3.connect('homeworkDB.db')
    cur = conn.cursor()

    cur.execute("INSERT INTO homeworks(title, mainText) VALUES('%s', '%s');" % (t, mt))
    conn.commit()
