import sqlite3
import uuid

def generaterandomid():
    ids=str(uuid.uuid1()) 
    return ids

def writeout(randomid, name, email, phone, message):
    con = sqlite3.connect('static/info.db')
    cur = con.cursor()
    cur.execute('INSERT INTO information (id, name, email, phone, message )VALUES (?, ?, ?, ?, ?)', (randomid, name, email, phone, message))
    con.commit()
