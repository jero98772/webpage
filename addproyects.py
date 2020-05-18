from flask import Flask, render_template, request, flash, redirect ,session,abort
from flask_socketio import  SocketIO, send
from flask_sqlalchemy import SQLAlchemy
import random
import os
import sqlite3
from codes_python import  gpgforall 

app=Flask(__name__)
webpage="/proyects"
socketio = SocketIO(app)
db=SQLAlchemy(app)
app.secret_key = "mysecretkey"
app.config['SECRET_KEY']
#app.secret_key = os.urandom(12)

def shortcut():
	connection = sqlite3.connect('personalweb')
	db = connection.cursor()
	return db
#====================== shorcuts

@app.route(webpage+"/")
def index():
	return render_template(webpage+"/index.html")
@app.route(webpage+"/donacionbtc.html")
def donacionbtc():
	return render_template(webpage+"/donacionbtc.html")

#====================== index or info
 
@app.route(webpage+"/aircolombia.html")
def aircolombia():
	return render_template(webpage+"/aircolombia.html")

@app.route(webpage+"/bechmarck.html")
def bechmarck():
	return render_template("bechmarck/bechmarck.html")
@app.route(webpage+"/bechmarck/bechmarckmulticore.html")
def bechmarckmulticore():
	start = time.time()
	nm=8500
	w = wwwof.wwwof()
	result = w.matrix(-nm,nm,(nm,nm))
	finish = time.time()
	return render_template("proyects/bechmarck/bechmarckmulticore.html", start = start , finish = finish, reply = result)

@app.route(webpage+"/bechmarck/bechmarcksinglecore.html")
def bechmarcksinglecore():
	start = time.time()
	result = 10**10**6 # not nesari import wwwof code for 1 line 
	finish = time.time()
	print(finish-start)
	return render_template("proyects/bechmarck/bechmarcksinglecore.html", start = start , finish = finish, reply = result)
@app.route(webpage+"/gpgforall.html")
#====================== litles proyest

def criptoforyou():
	#from codes_python import  gpgforall
	return render_template(webpage+"/gpgforall.html") 
@app.route(webpage+"/gpgforallfreemode.html" ,methods=['GET','POST'])
def criptoforyoufreemode():

	gpg4a = gpgforall.gpgforall()
	chars = gpg4a.collectionschars
	key = int(random.random()*1000%len(chars))
	cesartext =""
	mesaje = ""
	returntext = ""
	option = ""
	if request.method == 'POST':
		returntext = ""
		file = request.files["file"]
		try:
			option = str(request.form["optioncesar"])
		except:
			pass
		key = int(request.form["key"])
		cesartext = str(request.form["cesartext"])
		charshtml = str(request.form["chars"])
		chars = charshtml
		texttosha = str(request.form["sha256"])
		returntext =str(gpg4a.sha256aplay(texttosha))
		if option == "cifrate":
			"""
			for char in cesartext:
				num = chars.find(char) + key
				mod = int(num) % len(chars)
				mesaje = mesaje + (chars[mod])
			"""
			mesaje,key   = gpg4a.cifrar(cesartext, key,str( charshtml))
		elif option == "desifrate":
			"""
			for char in cesartext:
				num = chars.find(char) - key
				mod = int(num) % len(chars)
				mesaje = mesaje + (chars[mod])
			"""
			mesaje,key  = gpg4a.descifrar(cesartext, key,str( charshtml))
		else:
			mesaje = ""
	return render_template(webpage+"/gpgforallfreemode.html",charshtml = chars,resulthtml = mesaje,htmlkey=key,returnsha=returntext) 
@app.route(webpage+"/gas.html", methods = ['GET','POST'])
def gas():
	db = shortcut()
	#try:

	#except:
	#	pass
	if not session.get('loged'):
		return render_template(webpage+'/gas/gas_login.html')	
	else:
		user = session.get('user')
		db.execute(" SELECT * FROM gastos"+user)
		rows = db.fetchall()
		if request.method == 'POST':
			price = float(request.form["price"])
			thing = str(request.form["thing"])
			img = request.files.get("img_factura")
			values = [price,thing]
			user = session.get('user')
			valuesstr = ['price','thing']
			db.execute("INSERT INTO gastos{0}  (price,thing) VALUES ({1},'{2}');".format(user,price,thing ))
			db.connection.commit()
			db.close()
			return redirect(webpage+"/gas.html")
		return render_template(webpage+'/gas/gas.html',purchases = rows)	
	
	#return render_template(webpage+'/gas/gas.html')	
	#return appproyects

@app.route(webpage+"/gas_login.html", methods=['GET', 'POST'])
def gaslogin():	
	gpg4a = gpgforall.gpgforall()

	db = shortcut()
	db.execute(" SELECT usr FROM login")
	users = db.fetchall()
	db.execute(" SELECT pwd FROM login")
	pwd = db.fetchall()
	db.execute(" SELECT * FROM login")
	rows = db.fetchall()
	db.close()
	protectpwd = str(request.form["password"])
	protectpwd = str(gpg4a.sha256aplay(protectpwd))
	usr = request.form['username']
	for i in range(len(rows)):
		if usr in users[i] and protectpwd in pwd[i]  :
			session['loged'] = True
			session['user'] = usr
			return redirect("/proyects/")
		else:
			flash('wrong password!')
	return gas()

if __name__=='__main__':
	app.secret_key = os.urandom(12)
	app.run(debug=True,host="0.0.0.0")


