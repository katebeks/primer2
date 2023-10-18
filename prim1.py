import sqlite3
conn = sqlite3.connect("database1.db")
currs = conn.cursor()
#zaprosdb = """CREATE TABLE Konfirentia(Name TEXT, dataprovedenia TEXT, point TEXT, Organozatori TEXT, dniprovedenia INTEGER, Uchastvuut INTEGER, Dokladchiki INTEGER);"""
zaprosdb = """CREATE TABLE IF NOT EXISTS Konfirentia(Name TEXT, dataprovedenia TEXT, point TEXT, Organozatori TEXT, dniprovedenia INTEGER, Uchastvuut INTEGER, Dokladchiki INTEGER);"""
conn.execute(zaprosdb)
conn.commit()
insert1 = """INSERT INTO Konfirentia values ("Geografii", "01.06.2023", "Miskorena", "BGU", "3", "6", "3")"""
conn.execute(insert1)
conn.commit()
insert1 = """INSERT INTO Konfirentia values ("Biologii", "03.06.2023", "Miskorena", "BGPU", "3", "8", "4")"""
conn.execute(insert1)
conn.commit()
insert1 = """INSERT INTO Konfirentia values ("Himii", "02.06.2023", "Miskorena", "BPGU", "4", "6", "3")"""
conn.execute(insert1)
conn.commit()
insert1 = """INSERT INTO Konfirentia values ("Ingenernaia", "03.06.2023", "Miskorena", "BNTU", "3", "7", "3")"""
conn.execute(insert1)
conn.commit()
insert1 = """INSERT INTO Konfirentia values ("Ekologii", "01.06.2023", "Miskorena", "BGU", "3", "10", "7")"""
conn.execute(insert1)
conn.commit()
currs.close()
conn.close()