from flask import Flask, render_template, request, redirect, url_for, flash, Session  # Import Flask to allow us to create our app, and import
                                          # render_template to allow us to render index.html.
app = Flask(__name__)                     # Global variable __name__ tells Flask whether or not we
app.secret_key = 'hello'                                          # are running the file directly or importing it as a module.
@app.route('/')                           # The "@" symbol designates a "decorator" which attaches the
                                          # following function to the '/' route. This means that
                                          # whenever we send a request to localhost:5000/ we will run
                                          # the following "hello_world" function.
def home():
  return render_template("index.html")    # Render the template and return it!

@app.route('/results', methods=['POST'])

def results() :

  if len(request.form['name']) < 1 and len(request.form['comment']) < 1 :
    flash("Name can't be empty!")  
    flash("Comment can't be empty!")
    return redirect('/')
  elif len(request.form['name']) < 1 and len(request.form['comment']) > 120 :
    flash("Name can't be empty!")  
    flash("Comment is too long!")
    return redirect('/')
  elif len(request.form['name']) < 1 :
    flash("Name can't be empty!")  
    return redirect('/')     
  elif len(request.form['comment']) < 1 :
    flash("Comment can't be empty!")
    return redirect('/')
  elif len(request.form['comment']) > 120 :
    flash("Comment is too long!")
    return redirect('/')
  name = request.form['name']
  location = request.form['location']
  language = request.form['language']
  comment = request.form['comment']
  # else :
    
    # return redirect(url_for('home', name = request.form['name']))
  return render_template('results.html', name=name, location=location, language=language, comment=comment)
app.run(debug=True) 