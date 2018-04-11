from flask import Flask, render_template, request, redirect, url_for, session
# import the Connector function
from mysqlconnection import MySQLConnector
import datetime
app = Flask(__name__)
app.secret_key = 'hello'
# connect and store the connection in "mysql"; note that you pass the database name to the function
mysql = MySQLConnector(app, 'mydb')
# an example of running a query
# print mysql.query_db("SELECT * FROM users")
@app.route('/')

def home() :
    if 'validate' not in session :
        session['validate'] = 0
    return render_template('index.html')

@app.route('/success', methods=['GET', 'POST'])

def success() :
    if request.method == 'POST' :   
        email = request.form['email']
        q =   "SELECT * FROM users WHERE email = :email"
        data = {
                    'email': request.form['email'],
                }
        users = mysql.query_db(q,data)
        if len(users) == 0 :
            session['validate'] = 0
            query = "INSERT INTO users (email, created_at) VALUES (:email, DATE(NOW()))"
            mysql.query_db(query, data)
            return redirect('/success')
        else :
            session['validate'] = 1
            return redirect('/')
    else :
        users = mysql.query_db("SELECT * FROM users")
        return render_template('success.html', users = users)
    
app.run(debug=True)