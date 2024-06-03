from start import helper
helper()
import sqlite3

#CREATE CONNECTION OBJECT
con = sqlite3.connect("titanic.db")

# CREATE CURSOR OBJECT
curs = con.cursor()

# CREATE NEW TABLE
curs.execute('''CREATE TABLE new_table (
  name TEXT,
  age INTEGER,
  username TEXT,
  pay_rate REAL)''')

# INSERT ROW OF VALUES INTO TABLE
curs.execute('''INSERT INTO new_table VALUES ('Bob Peterson', 34, 'bob1234', 40.00)''')

# NEW ROWS OBJECT
new_rows = [('Anne Smith', 33, 'AS896', 25.00),
            ('Billy Roberts', 29, 'bill5Rob', 30.00),
            ('Jason Johnson', 48, 'JasonJ77', 40.00),
            ('Tim Trunk', 51, 'Timtrunk4', 40.00),
            ('Sarah Fall',19, 'SFall232', 25.00)
            ]

# INSERT NEW ROWS INTO TABLE
curs.executemany('''INSERT INTO new_table VALUES (?,?,?,?)''', new_rows)

# PULL THE FIRST ROW
one = curs.execute("SELECT * FROM titanic").fetchone()
# print(one)

# PULL THE FIRST TEN ROWS
ten = curs.execute("SELECT * FROM titanic").fetchmany(10)
# print(ten)

# PULL EVERY ROW
all_rows = curs.execute("SELECT * FROM titanic").fetchall()
# print(all_rows)

# PULL EVERY ROW FOR THOSE WHO SURVIVED
all_survived = curs.execute('''SELECT * FROM titanic WHERE Survived = 1;''').fetchall()
# print(all_survived)

# PULL ALL AGE RECORDS
age = curs.execute("SELECT Age FROM titanic;").fetchall()

sum = 0

# COUNTS THE NUMBER OF PEOPLE UNDER 18
for num in age:
  if num[0] < 18:
    sum += 1 
# print(sum)

# INSERT ROW OF VALUES INTO TABLE
curs.execute('''INSERT INTO new_table VALUES ('Stephanie Bready', 37, 'stephB423', 30.00)''')

# PULL SPECIFIC ROW
n_row = curs.execute('''SELECT * FROM new_table WHERE username = 'stephB423';''').fetchone()

# COMMIT THIS CHANGE
con.commit()

# CLOSE THE CONNECTION
con.close()
