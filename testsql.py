#I WILL ASSUME THAT YOU ALREADY KNOW HOW TO INSTALL AND CONFIGURE XAMPP AND MYSQL#
#import required libraries

import mysql.connector


###connect to your mysql server####

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="dede"
)


#add data you want to the exact table#

cursor = db.cursor()
sql = "INSERT INTO initabel (id, nama, alamat,stok) VALUES (%s, %s,%s, %s)"

values = [
 ("b4", "dede","bandung","198"),
 ("b5", "Rawr","kota muda","10"),
 ("b6", "Unch","Tangerang","165"),
 
]
for val in values:
  cursor.execute(sql, val)
  db.commit()

print("{} data added".format(len(values)))
