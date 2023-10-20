import sqlite3
conn = sqlite3.connect("database1.db")
currs = conn.cursor()
#zaprosdb = """CREATE TABLE Konfirentia(Name TEXT, dataprovedenia TEXT, point TEXT, Organozatori TEXT, dniprovedenia INTEGER, Uchastvuut INTEGER, Dokladchiki INTEGER);"""
zaprosdb = """SELECT * FROM Uchaqsniki WHERE kafedra='himii-biologii';"""
currs.execute(zaprosdb)
rez = currs.fetchall()
for i in rez:
    print(i)
#print(rez)
currs.close()
conn.close()