from flask import Flask, render_template, request, redirect, url_for, session  # Import Flask to allow us to create our app, and import
                                          # render_template to allow us to render index.html.
app = Flask(__name__)                     # Global variable __name__ tells Flask whether or not we
app.secret_key = 'hello'                                          # are running the file directly or importing it as a module.
@app.route('/')                           # The "@" symbol designates a "decorator" which attaches the
                                          # following function to the '/' route. This means that
                                          # whenever we send a request to localhost:5000/ we will run
                                          # the following "hello_world" function.
def home():
  if 'count' not in session :
    session['count'] = 0
  else :
    session['count'] += 1
  return render_template("index.html", count=session['count'])    # Render the template and return it!

@app.route('/extra')

def extra() :
  session['count'] += 1
  return redirect('/')

@app.route('/reset')

def reset() :
  session.clear()
  return redirect('/')
# @app.route('/ninja') 

# def ninjas() :
#   ninjas = 'tmnt.png'
#   return render_template('ninja.html', ninjas=ninjas)

app.run(debug=True) 