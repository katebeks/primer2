import sqlite3
conn = sqlite3.connect("database1.db")
currs = conn.cursor()
zaprosdb = """CREATE TABLE Konfirentia(Name TEXT, dataprovedenia TEXT, point TEXT, Organozatori TEXT, dniprovedenia INTEGER, Uchastvuut INTEGER, Dokladchiki INTEGER);"""
conn.execute(zaprosdb)
conn.commit()
currs.close()
conn.close()