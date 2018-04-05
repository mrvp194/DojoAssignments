from flask import Flask, render_template, request, redirect, url_for  # Import Flask to allow us to create our app, and import
                                          # render_template to allow us to render index.html.
app = Flask(__name__)                     # Global variable __name__ tells Flask whether or not we
                                          # are running the file directly or importing it as a module.
@app.route('/')                           # The "@" symbol designates a "decorator" which attaches the
                                          # following function to the '/' route. This means that
                                          # whenever we send a request to localhost:5000/ we will run
                                          # the following "hello_world" function.
def home():
  return render_template("index.html")    # Render the template and return it!

@app.route('/ninja') 

def ninjas() :
  ninjas = 'tmnt.png'
  return render_template('ninja.html', ninjas=ninjas)

@app.route('/ninja/<color>')

def ninja(color) :
  if color == 'blue' :
    ninjas = "leonardo.jpg"
  elif color == 'purple' :
    ninjas = 'donatello.jpg'
  elif color == 'red' :
    ninjas = "raphael.jpg"
  else :
    ninjas = "michelangelo.jpg"
  return render_template('ninja.html', ninjas=ninjas)

app.run(debug=True) 