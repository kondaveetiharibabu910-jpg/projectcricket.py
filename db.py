import sqlite3

conn = sqlite3.connect("student.db", check_same_thread=False)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS student(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    t20score INTEGER,
    testscore INTEGER,
    odiscore INTEGER,
    toprank INTEGER
)
""")
conn.commit()


def insert_record(name, t20score, testscore, odiscore, toprank):
    cur.execute(
        """
        INSERT INTO student
        (name, t20score, testscore, odiscore, toprank)
        VALUES(?,?,?,?,?)
        """,
        (name, t20score, testscore, odiscore, toprank)
    )
    conn.commit()
    return "Record Inserted Successfully"


def retrieve_record(id):
    cur.execute("SELECT * FROM student WHERE id=?", (id,))
    return cur.fetchone()


def update_record(id, name, t20score, testscore, odiscore, toprank):
    cur.execute(
        """
        UPDATE student
        SET
            name=?,
            t20score=?,
            testscore=?,
            odiscore=?,
            toprank=?
        WHERE id=?
        """,
        (name, t20score, testscore, odiscore, toprank, id)
    )

    conn.commit()

    if cur.rowcount > 0:
        return "Record Updated Successfully"
    else:
        return "Record Not Found"


def display_records():
    cur.execute("SELECT * FROM student")
    return cur.fetchall()


def delete_record(id):
    cur.execute("DELETE FROM student WHERE id=?", (id,))
    conn.commit()

    if cur.rowcount > 0:
        return "Record Deleted Successfully"
    else:
        return "Record Not Found"
















    

    























