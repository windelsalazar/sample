from tkinter import *
import psycopg2 




try: 
    conn = psycopg2.connect(database="crud", user="postgres", password="windel1325", host="localhost")
    print("connected")
except:
    print ("I am unable to connect to the database")


cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS emp  (id serial PRIMARY KEY, employee varchar, branch varchar, designation varchar, salary integer);")
#cur.execute("INSERT INTO emp (employee, branch, designation, salary) VALUES (%s, %s, %s, %s)")


conn.commit()


cur.close()

conn.close()