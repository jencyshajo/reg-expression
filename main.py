import sqlite3

conn = sqlite3.connect('test.db') # will create db authomatically



conn.execute('''
    CREATE TABLE COMPANY
    (Id INT PRIMARY KEY NOT NULL,
    NAME    TEXT        NOT NULL,
    AGE     INT         NOT NULL,
    ADDRESS CHAR (50),
    SALARY  REAL);''')



conn.execute("INSERT INTO COMPANY (ID, Name, AGE, ADDRESS, SALARY)\
             VALUES (1, 'Anna', 35, 'London', 10000.00)");
conn.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY)\
             VALUES (2, 'John', 25, 'Linchfield', 85000.00)");
conn.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY)\
             VALUES (3, 'Maria', 29, 'Cambridge', 60000.00)");
conn.commit()
print("Records created successfully")







