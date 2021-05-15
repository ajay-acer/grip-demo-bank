import sqlite3
import pandas as pd


data = {
    "Name": ['Liam', 'Olivia', 'Noah','Emma','Oliver','Ava','Elijah','Charlotte','William','Sophia'],
    "Account_no": [5144256745896, 5144256745886, 5144256745897,5144256745899,5144256745596,5144256745876,5144256745898,5144256745816,5144256745891,5144256745890],
    "Balance":[5000.0,300.0,2000.0,4000.0,5000.0,10000.0,20000.0,3000.0,400.0,7000.0],
    "Email":['liam@gmail.com','olivia@hotmail.com','noah45@gmail.com','emma@yahoo.com','oliver@hotmail.com','ava77@gmail.com','elijah@yahoo.com','charlotte@gmail.com','william@gmail.com','sophia@hotmail.com']
  }

df = pd.DataFrame(data)

conn = sqlite3.connect('BankDB.db')  
c = conn.cursor()

c.execute('''CREATE TABLE BANK([Name] TEXT,[Account_no] INTEGER,[Balance] REAL,[Email] TEXT)''')

df.to_sql('BANK',conn,if_exists='replace',index=False)

c.execute('''Select * from BANK''')


conn = sqlite3.connect('BankDB.db')  

c.execute('''CREATE TABLE HISTORY([From] TEXT,[To] TEXT,[Amount] REAL)''')

print(c.fetchall)

conn.commit()
conn.close()

