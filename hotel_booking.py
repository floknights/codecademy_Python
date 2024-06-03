# IMPORT MODULE
import sqlite3

# CREATE CONNECTION OBJECT
con = sqlite3.connect("hotel_booking.db")

# CREATE CURSOR OBJECT
cur = con.cursor()

# VIEW FIRST ROW OF booking_summary
print(cur.execute('''SELECT * FROM booking_summary''').fetchone())

# VIEW FIRST 10 ROWS OF booking_summary 
print(cur.execute("SELECT * FROM booking_summary").fetchmany(10))

# CREATE OBJECT bra AND PRINT FIRST 5 ROWS TO CHECK DATA
bra = cur.execute('''SELECT * FROM booking_summary WHERE country = 'BRA';''').fetchall()
print(bra)

# CRAETE NEW TABLE CALLED bra_customers
cur.execute('''CREATE TABLE IF NOT EXISTS bra_customers (
  num INTEGER,
  hotel TEXT,
  is_cancelled INTEGER,
  lead_time INTEGER,
  arrival_date_year INTEGER,
  arrival_date_month TEXT,
  arrival_date_day_of_month INTEGER, 
  adults INTEGER,
  children INTEGER,
  country TEXT,
  adr REAL,
  special_requests INTEGER)''')

# INSERT THE OBJECT bra INTO THE TABLE bra_customers 
cur.executemany('''INSERT INTO bra_customers VALUES (?,?,?,?,?,?,?,?,?,?,?,?)''', bra)

# VIEW THE FIRST 10 ROWS OF bra_customers
print(cur.execute("SELECT * FROM bra_customers").fetchmany(10))

# RETRIEVE lead_time ROWS WHERE THE BOOKINGS WERE CANCELLED
lead_time_can = cur.execute('''SELECT lead_time FROM bra_customers WHERE is_cancelled = 1;''').fetchall()

# FIND AVERAGE LEAD TIME FOR THOSE WHO CANCELLED
sum = 0
for num in lead_time_can:
  sum += num[0]

lead_time_can_avg = sum/len(lead_time_can)

# PRINT RESULTS
print(lead_time_can_avg)

# RETRIEVE lead_time ROWS WHERE THE BOOKINGS WERE NOT CANCELLED
lead_time = cur.execute('''SELECT lead_time FROM bra_customers WHERE is_cancelled = 0;''').fetchall()

# FIND AVERAGE LEAD TIME FOR THOSE WHO DID NOT CANCEL
sum = 0
for num in lead_time:
  sum += num[0]

lead_time_avg = sum/len(lead_time)

# PRINT RESULTS
print(lead_time_avg)

# RETRIEVE special_requests ROWS WHERE THE BOOKINGS WERE CANCELLED
special_requests_can = cur.execute('''SELECT special_requests FROM bra_customers WHERE is_cancelled = 1;''').fetchall()

# FIND TOTAL SPECIAL REQUESTS FOR THOSE WHO CANCELLED
count_can = 0
for num in special_requests_can:
  count_can += 1

# PRINT RESULTS
print(count_can)

# RETRIEVE special_requests ROWS WHERE THE BOOKINGS WERE NOT CANCELLED
special_requests = cur.execute('''SELECT special_requests FROM bra_customers WHERE is_cancelled = 0;''').fetchall()

# FIND TOTAL SPECIAL REQUESTS FOR THOSE WHO DID NOT CANCEL
count = 0
for num in special_requests:
  count += 1

# PRINT RESULTS
print(count)

# COMMIT CHANGES AND CLOSE THE CONNECTION
con.commit()
con.close()
