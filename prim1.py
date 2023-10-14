import sqlite3
conn = sqlite3.connect("database1.db")
currs = conn.cursor()
zaprosdb = """CREATE TABLE IF NOT EXISTS Konfirentia(Name TEXT, dataprovedenia TEXT, point TEXT, Organozatori TEXT, dniprovedenia INTEGER, Uchastvuut INTEGER, Dokladchiki INTEGER);"""
conn.execute(zaprosdb)
conn.commit()
insert1 = """INSERT INTO Uchaqstie values ("Pavlov Ivan", "13.05.2023", "14.05.2023", "razvitie organizmov", "sintez, razvitie", "30.05.2023", "yes", "5.06.2023")"""
conn.execute(insert1)
conn.commit()
insert1 = """INSERT INTO Uchaqstie values ("Garavin Alexsandr", "13.05.2023", "14.05.2023", "migracii zhivotnih", "pereselenie, migracia, osedlie zhivotnie", "30.05.2023", "yes", "5.06.2023")"""
conn.execute(insert1)
conn.commit()
insert1 = """INSERT INTO Uchaqstie values ("Petrova Valentina", "13.05.2023", "13.05.2023", "metodika obuchenia biologii", "objee chasnoe metodi", "30.05.2023", "yes", "5.06.2023")"""
conn.execute(insert1)
conn.commit()
insert1 = """INSERT INTO Uchaqstie values ("Pavlov Ivan", "13.05.2023", "13.05.2023", "uslovia razmnozhenia organozmov", "sintez, razmnozhenie", "30.05.2023", "yes", "5.06.2023")"""
conn.execute(insert1)
conn.commit()
insert1 = """INSERT INTO Uchaqstie values ("Povilina Irina", "13.05.2023", "13.05.2023", "metodika obuchenia biologii", "objee chasnoe metodi", "30.05.2023", "yes", "5.06.2023")"""
conn.execute(insert1)
conn.commit()
currs.close()
conn.close()