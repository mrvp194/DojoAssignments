from flask import Flask, render_template, request, redirect, url_for, session  # Import Flask to allow us to create our app, and import
import random                                          # render_template to allow us to render index.html.
app = Flask(__name__)                     # Global variable __name__ tells Flask whether or not we
app.secret_key = 'hello'                                          # are running the file directly or importing it as a module.
@app.route('/')                           # The "@" symbol designates a "decorator" which attaches the
                                          # following function to the '/' route. This means that
                                          # whenever we send a request to localhost:5000/ we will run
                                          # the following "hello_world" function.
def home():
  if 'num' not in session :
    session['num'] = random.randrange(0,101)
  if 'guess' in session :
    guess = session['guess']
  else :
    guess = 0
  print session['num']
  return render_template("index.html", num=session['num'], guess=guess)    # Render the template and return it!

@app.route('/guess', methods=['POST'])

def guess() :
  guess = request.form['guess']
  print guess
  print session['num']
  if int(guess) > session['num'] :
    session['guess'] = 'too high'
  elif int(guess) < session['num'] :
    session['guess'] = 'too low'
  elif int(guess) == session['num'] :
    session['guess'] = 'correct'
  print session['guess']
  return redirect('/')

@app.route('/reset') 

def reset() :
  session.clear()
  return redirect('/')
app.run(debug=True) 