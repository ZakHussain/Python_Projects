from flask import Flask, render_template, redirect, request, session, flash

app = Flask(__name__)
app.secret_key = 'letssharesecrets'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/ninja')
def ninjas():
	
	return render_template('ninja.html', displayAll = True)


@app.route('/ninja/<color>')
def show_ninja_image(color):
	return render_template("ninja.html", color=color, displayAll=False)


app.run(debug=True)