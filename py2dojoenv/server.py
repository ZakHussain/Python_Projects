from flask import Flask, render_template, request, redirect, session, flash 
app = Flask(__name__)
app.secret_key='Iamtired'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/result', methods=['POST'])
def create_result():
	session['name'] = request.form['name']
	session['city'] = request.form['city']
	session['language']= request.form['language']
	session['comment'] = request.form['comment']

	#create if else statement

	if len(session['name'])<1:
		flash("Name cannot be empty!")
	if len(session['comment'])>10:
		flash("length of comment must be under 120 characters!")
	elif (len(session['name'])<0 and len(session['comment']))<11:
		flash("Success! your name is {} and you left a comment saying {}".format((session['name']), session['comment']))

	return redirect('/process')

@app.route('/process')
def show_user():
	return render_template('results.html')

app.run(debug=True)
