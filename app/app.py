from flask import Flask,render_template,request  
import pandas as pd
import sqlite3

app = Flask(__name__)

@app.route('/')   
def home():
    return render_template('index.html')

@app.route('/view')
def view(): 
    with sqlite3.connect("BankDB.db") as conn:
        c = conn.cursor()
        c.execute('''SELECT * FROM BANK''')
        df=pd.DataFrame(c.fetchall(), columns=['Name','Account_no','Balance','Email'])
        return render_template('grip.html',df=df) 
    

@app.route('/transfer',methods=['POST'])
def transfer():
    form_data=request.form
    fr=form_data['from']
    amt=form_data['amt']
    t=form_data['to']
    print(form_data)
    with sqlite3.connect("BankDB.db") as conn:
        c = conn.cursor()
        c.execute('''UPDATE BANK SET Balance=Balance-? where Name=? and Balance>=?''',(amt,fr,amt))
        if conn.total_changes==0:
            return render_template('failed.html')
        c.execute('''UPDATE BANK SET Balance=Balance+? where Name=?''',(amt,t,))
        conn.commit()
        c.execute('''INSERT INTO HISTORY VALUES(?,?,?) ''',(fr,t,amt))
        return render_template('success.html') 

@app.route('/history')
def history():
    with sqlite3.connect("BankDB.db") as conn:
        c = conn.cursor()
        c.execute('''SELECT * FROM HISTORY''')
        df=pd.DataFrame(c.fetchall(), columns=['From','To','Amount'])
        return render_template('transhist.html',df=df)
