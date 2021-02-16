import psycopg2

con = psycopg2.connect(
            host = "localhost" ,  
            database = "mydatabase",
            user = "postgres",
            password = "windel1325")


cur = con.cursor()

cur.execute("insert into customers (id, name) values(%s, %s)", (9, "kobe bolokdoy")) 

cur.execute("select id, name from customers")

rows = cur.fetchall()

for r in rows:
     print (f"id {r[0]} name {r[1]}")

con.commit()

cur.close()



con.close()