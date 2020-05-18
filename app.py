#import www_of
from flask import Flask, render_template, request, flash, redirect ,session
import subprocess
try:
	from flask_sqlalchemy import SQLAlchemy
#from wtforms import  BooleanField, StringField, validators ,IntegerField
	import psycopg2, psycopg2.extras
	from psycopg2.extensions import AsIs
except:	
	subprocess.run("systemctl start postgresql.service", shell =True)
#from flask_sqlalchemy import SQLAlchemy
import time
import numpy as np
import os
import urllib.request
import cv2
#from werkzeug.utils import secure_filename

from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
from tensorflow.python.keras import optimizers
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dropout, Flatten, Dense, Activation
from tensorflow.python.keras.layers import  Convolution2D, MaxPooling2D
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model
from tensorflow.python.keras import backend as K
from codes_python import ordenador
#from flask_dropzone import Dropzone
#from codes_python.gpgforall import pseudorandom
from codes_python import wwwof 
from addproyects import app as appproyects
from www_of import app as appwwwof
import sqlite3
from codes_python import  gpgforall 


strwwwof = "/www_of/"
proyects = "/proyects/"
howproyects = "howproyects"
app=Flask(__name__)
db=SQLAlchemy(app)

app.secret_key = os.urandom(12)
def shortcut():
	connection = sqlite3.connect('personalweb')
	db = connection.cursor()
	return db
gpg4a = gpgforall.gpgforall()

@app.route("/")
def index():
	return render_template("index.html")
@app.route("/blog")
def blog():
	return render_template("blog.html")  
@app.route("/donacionbtc.html" )
def donations():
	return render_template("donacionbtc.html")

@app.route(strwwwof+"donacionbtc.html" )
def donationsappwwwof():
	return appwwwof

@app.route(proyects+"donacionbtc.html" )
def donationsappproyects():
	return appproyects
#===========================proyects
@app.route(proyects+"/")
def proyectsindex():
	return render_template(proyects+"/index.html")
@app.route(proyects+"aircolombia.html")
def aircolombia():
	return appproyects
@app.route(proyects+"gpgforall.html")
def criptoforyou():
	return appproyects
@app.route(proyects+"gpgforallfreemode.html",methods=['GET', 'POST'])
def criptoforyoufreemode():
	return appproyects
@app.route(proyects+"gas.html", methods = ['GET','POST'])
def gas():

	return appproyects
@app.route(proyects+"gas_login.html", methods=['POST'])
def gaslogin():
	return appproyects

#===========================wwwof
@app.route(strwwwof)
def wwwof():
	return appwwwof
@app.route(strwwwof+"curapeces.html" , methods=['GET','POST'])
def curapeces():
	return appwwwof
@app.route(strwwwof+"calcupH.html" )
def calcuph():
	return appwwwof
@app.route(strwwwof+"drawFISHTANK.html" )
def drawFISHTANK():
	return appwwwof
@app.route(strwwwof+"data_basecsv.html", methods=['GET','POST'] )
def data_basecsv():
	return appwwwof

@app.route(strwwwof+"data_basecsv/delete/<string:id>", methods=['GET','POST'])
def delete(id):
	return appwwwof
@app.route(strwwwof+'data_basecsv/actualisar<string:id>', methods=['GET','POST'])
def update_fish(id):
	return appwwwof

@app.route(strwwwof+'data_basecsv/<string:id>', methods=['GET','POST'])
def get_fish(id):
	return appwwwof
@app.route(strwwwof+"divePC.html" )
def divePC():
	return appwwwof

@app.route(strwwwof+howproyects+"/howcalcupH.html")
def howcalcuph():
	return appwwwof
@app.route(strwwwof+howproyects+"/howdrawFISHTANK.html")
def howdrawfishtank():
	return appwwwof 
@app.route(strwwwof+howproyects+"/howcurapeces.html")
def howcurapeces():
	return appwwwof 
@app.route(strwwwof+howproyects+"/howfishdb.html")
def howfishdb():
	return appwwwof
@app.route(strwwwof+"valores.html") 
def valoreswwwof():
	return appwwwof
@app.route(strwwwof+"planeacion.html")
def planeacionwwwof():
	return appwwwof	
@app.route(strwwwof+"informe_de_ensayos.html")
def informe_de_ensayoswwwof():
	return appwwwof
@app.route(strwwwof+"tecnologias.html") 
def tecnologiaswwwof():
	return appwwwof

'''
@app.route("/gaslogin", methods=['POST'])
def gaslogin():
	db = shortcut()
	"""
	db.execute(" SELECT usr FROM login")
	users = db.fetchall()
	db.execute(" SELECT pwd FROM login")
	pwd = db.fetchall()
	"""
	db.execute(" SELECT * FROM login")
	rows = db.fetchall()
	db.close()
	password = str(request.form["password"])
	protectpwd = str(gpg4a.sha256aplay(password))
	usr = request.form['username']
	print("\n",rows)
	for i in range(len(rows[0])):
		if urs == rows[0][i] and protectpwd  == rows[1][i]  :
			session['loged'] = True
		else:
			flash('wrong password!')
	return index()
'''
if __name__=='__main__':
	app.run(debug=True,host="0.0.0.0")
