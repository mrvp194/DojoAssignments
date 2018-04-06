from flask import Flask, render_template, request, redirect, url_for, session  # Import Flask to allow us to create our app, and import
import random                                          # render_template to allow us to render index.html.
app = Flask(__name__)                     # Global variable __name__ tells Flask whether or not we
app.secret_key = 'hello'                                          # are running the file directly or importing it as a module.
@app.route('/')                           # The "@" symbol designates a "decorator" which attaches the
                                          # following function to the '/' route. This means that
                                          # whenever we send a request to localhost:5000/ we will run
                                          # the following "hello_world" function.
def home():
  if 'gold' not in session :
    session['gold'] = 0
    session['activities'] = []
  
  
  
  return render_template("index.html", gold=session['gold'], activities=session['activities'])    # Render the template and return it!

@app.route('/process_money', methods=['POST'])

def money() :
  print session['activities']
  if 'farm' in request.form :
    gold = random.randrange(10,21)
    session['activities'].append('Earned {} gold from the farm!'.format(gold))
  elif 'cave' in request.form :
    gold = random.randrange(5,11)
    session['activities'].append('Earned {} gold from the cave!'.format(gold))
  elif 'house' in request.form :
    gold = random.randrange(2,6)
    session['activities'].append('Earned {} gold from the house!'.format(gold))  
  elif 'casino' in request.form :
    gold = random.randrange(-50,51)
    session['activities'].append('Earned {} gold from the casino!'.format(gold))
  session['gold'] += gold
  return redirect('/')

@app.route('/reset') 

def reset() :
  session.clear()
  return redirect('/')
app.run(debug=True) 