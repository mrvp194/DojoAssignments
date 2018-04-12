from flask import Flask, render_template, request, redirect, url_for, session
# import the Connector function
from mysqlconnection import MySQLConnector
import datetime 
import re
import md5
app = Flask(__name__)
app.secret_key = 'hello'
# connect and store the connection in "mysql"; note that you pass the database name to the function
mysql = MySQLConnector(app, 'mydb')
# an example of running a query
@app.route('/')

def home() :
    
    return render_template('index.html')

@app.route('/users/new')

def new() :

    return render_template('new.html')

@app.route('/users', methods=['POST'])

def user() :
    session['validation'] = ''
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'password' : request.form['password'],
        'confirmation' : request.form['confirmation']
            }

    if len(data['first_name']) < 2 or any(char.isdigit() for char in data['first_name']) :
        
        session['validation'] = 'Invalid First Name'
        return redirect('/users/new')
    
    elif len(data['last_name']) < 2 or any(char.isdigit() for char in data['last_name']) :
        session['validation'] = 'Invalid Last Name'
        return redirect('/users/new')
    
    elif len(data['email']) < 0 or re.match(r"[^@]+@[^@]+\.[^@]+", data['email']) == None :
        session['validation'] = 'Invalid Email'
        return redirect('/users/new')
    
    elif len(data['password']) < 8 :
        session['validation'] = 'Password Must Be at Least 8 Characters'
        return redirect('/users/new')
    elif data['password'] != data['confirmation'] :
        session['validation'] = 'Passwords did not match'
        return redirect('user/new')
    else :
        data['password'] = md5.new(data['password']).hexdigest()
        # print type(data['password'])
        # print data['password'].decode('utf-8')
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (:first_name, :last_name, :email, :password)"
        mysql.query_db(query, data)
        session['login'] = True
        session['validate'] = ''
        return redirect('/success')

@app.route('/success') 

def success() :
    return render_template('success.html')


@app.route('/login', methods=['GET', 'POST'])

def login() :
    if request.method == 'GET' :
        return render_template('login.html')
    else :
        data = {
            'email' : request.form['email'],
            'password' : request.form['password']
                }
        query = "SELECT * FROM users WHERE email = :email"
        user = mysql.query_db(query, data)
        if len(user) == 0 :
            session['validation'] = 'invalid email'
            return redirect('/login')
        else:
            if md5.new(data['password']).hexdigest() != user[0]['password'] :
                session['validation'] = 'invalid password'
                return redirect('/login')
            else :
                session['validation'] = ''
                session['login'] = True
                return redirect('/success')
        # if request.method == 'POST' :   
    #     email = request.form['email']
    #     q =   "SELECT * FROM users WHERE email = :email"
    #     data = {
    #                 'email': request.form['email'],
    #             }
    #     users = mysql.query_db(q,data)
    #     if len(users) == 0 :
    #         session['validate'] = 0
    #         query = "INSERT INTO users (email, created_at) VALUES (:email, DATE(NOW()))"
    #         mysql.query_db(query, data)
    #         return redirect('/success')
    #     else :
    #         session['validate'] = 1
    #         return redirect('/')
    # else :
    #     users = mysql.query_db("SELECT * FROM users")
    #     return render_template('success.html', users = users)
    
app.run(debug=True)