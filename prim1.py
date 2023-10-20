import sqlite3
conn = sqlite3.connect("database1.db")
currs = conn.cursor()
#zaprosdb = """CREATE TABLE Konfirentia(Name TEXT, dataprovedenia TEXT, point TEXT, Organozatori TEXT, dniprovedenia INTEGER, Uchastvuut INTEGER, Dokladchiki INTEGER);"""
zap1 = """UPDATE Uchaqsniki SET city='Gomel' WHERE rabota='BGPU';"""
currs.execute(zap1)
conn.commit()
zap2 = """DELETE FROM Uchaqsniki WHERE rabota='BGU';"""
currs.execute(zap2)
conn.commit()
zaprosdb = """SELECT * FROM Uchaqsniki;"""
currs.execute(zaprosdb)
rez = currs.fetchall()
for i in rez:
    print(i)
#print(rez)
currs.close()
conn.close()