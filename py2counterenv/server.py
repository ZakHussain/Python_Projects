from flask import Flask, render_template, request,  session, redirect
app = Flask(__name__)

app.secret_key ='ThisIsSecret'

def counter():
	try:	
		session['counter'] += 1
	except: 
		session['counter'] = 0

@app.route('/')
def index():
	counter()
	return render_template("index.html")
app.run(debug=True)