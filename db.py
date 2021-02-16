from tkinter import *
import psycopg2 

def fetch(cur):
    cur.execute("SELECT * FROM emp")
    rows = cur.fetchall()
    return rows

def insert(employee, branch, designation, salary):
    cur.execute("INSERT INTO emp VALUES (NULL, ?, ?, ?, ?)", (employee, branch, designation, salary))
    conn.commit()

def remove(id):
    cur.execute("DELETE FROM emp WHERE id=?", (id,))
    conn.commit()

def update(id, employee, branch, designation, salary):
    cur.execute("UPDATE emp set employee = ?, branch = ?, designation = ?, salary = ? WHERE id = ?", (employee, branch, designation, salary))
    conn.commit()

def clear_text(cur):
    conn.close()


try: 
    conn = psycopg2.connect(database="crud", user="postgres", password="windel1325", host="localhost")
    print("connected")
except:
    print ("I am unable to connect to the database")

cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS emp  (id serial PRIMARY KEY, employee varchar, branch varchar, designation varchar, salary integer);")
cur.execute("INSERT INTO emp (employee, branch, designation, salary) VALUES (%s, %s, %s, %s)")


conn.commit()


cur.close()

conn.close()