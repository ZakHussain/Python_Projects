from flask import Flask, render_template, redirect, session, request
import random 
app = Flask(__name__)
app.secret_key = "mylittlesecret"

@app.route('/')
def index():
	if 'gold'in session:
		pass
	else:
		session['gold'] = 0
	if 'message' in session:
		pass	
	else:
		session['message'] = []

	return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
	if request.form['building'] == 'farm':
		gold = random.randrange(10,21)
		session['gold']+= gold
		string = "you recieved "+str(gold)
		session['message'].append(string)
	if request.form['building'] == 'cave':
		gold = random.randrange(5,11)
		session['gold']+= gold
		string = "you recieved "+str(gold)
		session['message'].append(string)	
	if request.form['building'] == 'house':
		gold = random.randrange(2,6)
		session['gold']+= gold
		string = "you recieved "+str(gold)
		session['message'].append(string)
	if request.form['building'] == 'casino':
		gold = random.randrange(-50,51)
		session['gold']+= gold
		string = "you recieved "+str(gold)
		session['message'].append(string)
	if request.form['building'] == 'reset':
		session.clear()
	return redirect('/')
app.run(debug=True)