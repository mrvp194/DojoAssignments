from flask import Flask, render_template, request, redirect, url_for
# import the Connector function
from mysqlconnection import MySQLConnector
import datetime
app = Flask(__name__)
# connect and store the connection in "mysql"; note that you pass the database name to the function
mysql = MySQLConnector(app, 'mydb')
# an example of running a query
# print mysql.query_db("SELECT * FROM users")
@app.route('/')

def home() :
    users = mysql.query_db("SELECT * FROM users")

    return render_template('index.html', users = users)

@app.route('/friend', methods=['POST'])

def friend() :
    query = "INSERT INTO users (name, age, since) VALUES (:name, :age, :since)"
    # We'll then create a dictionary of data from the POST data received.
    data = {
             'name': request.form['name'],
             'age':  request.form['age'],
             'since': datetime.date.today()
           }
    mysql.query_db(query, data)
    return redirect('/')
    
app.run(debug=True)