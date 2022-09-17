import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="@Siva8124",
  database="mydatabase"
)


Cursor = mydb.cursor()
#Cursor.execute("CREATE DATABASE mydatabase") 
Cursor.execute("DROP TABLE IF EXISTS bankdetails")
Cursor.execute("""CREATE TABLE IF NOT EXISTS bankdetails (ACCOUNT_NO INT PRIMARY KEY NOT NULL,CARD_NO INT NOT NULL, NAME VARCHAR(255) NOT NULL,BALANCE INT NOT NULL,PIN VARCHAR(255))""")

Coloumns = "ACCOUNT_NO, CARD_NO, NAME, BALANCE, PIN "
Val = "980123467, 65538, 'SIVARAJ', 189898, 'Sivaraj'"
Val2 = "98012346, 65537, 'SUBA', 189898, 'Suba'"

Cursor.execute("INSERT INTO bankdetails (%s) VALUES (%s)"%(Coloumns,Val))
Cursor.execute("INSERT INTO bankdetails (%s) VALUES (%s)"%(Coloumns,Val2))
  
mydb.commit()

def Fetch(column, cardno):
    Cursor.execute("SELECT %s FROM bankdetails WHERE CARD_NO=%d"%(column,cardno))
    for i in Cursor:
        i = str(i)
        i = i[1:len(i)-2]
        return i

def updateData(coloumn, value, cardno):
    Cursor.execute("UPDATE bankdetails SET %s=%d where CARD_NO=%d"%(coloumn,value,cardno))
    mydb.commit()



