<<<<<<< HEAD
<<<<<<< HEAD
from flask import Flask,render_template,request

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/codeblog'



db = SQLAlchemy()
# dep(app)
#     return appf create_app():
#     app = Flask(__name__)
#     db.init_ap


class Contacts(db.Model):
    sno= db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),nullable=False)
    phone_num = db.Column(db.String(12),nullable=False)
    msg = db.Column(db.String(120),nullable=False)
    date = db.Column(db.String(12),nullable=True)
    email = db.Column(db.String(20),nullable=False)




@app.route('/')
def home():
    return render_template('index.html')
# app.run() 
@app.route('/about')
def about():
    return render_template('about.html')
# app.run() 
@app.route('/contact',methods=['GET','POST'])
def contact():
    if (request.method=='POST'):
        # add entry to the database
        name=request.form.get('name')
        email=request.form.get('email')
        phone=request.form.get('phone')
        message=request.form.get('message')
        # name=request.form.get('name')
        entry=Contacts(name=name,phone_num=phone,msg=message,date = datetime.now() , email=email)


        db.session.add(entry)
        db.session.commit()
    return render_template('contact.html')
# app.run() 
# @app.route('/post')
# def post():
#     return render_template('post.html')
 

=======
from flask import Flask,render_template,request

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/codeblog'



db = SQLAlchemy()
# dep(app)
#     return appf create_app():
#     app = Flask(__name__)
#     db.init_ap


class Contacts(db.Model):
    sno= db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),nullable=False)
    phone_num = db.Column(db.String(12),nullable=False)
    msg = db.Column(db.String(120),nullable=False)
    date = db.Column(db.String(12),nullable=True)
    email = db.Column(db.String(20),nullable=False)




@app.route('/')
def home():
    return render_template('index.html')
# app.run() 
@app.route('/about')
def about():
    return render_template('about.html')
# app.run() 
@app.route('/contact',methods=['GET','POST'])
def contact():
    if (request.method=='POST'):
        # add entry to the database
        name=request.form.get('name')
        email=request.form.get('email')
        phone=request.form.get('phone')
        message=request.form.get('message')
        # name=request.form.get('name')
        entry=Contacts(name=name,phone_num=phone,msg=message,date = datetime.now() , email=email)


        db.session.add(entry)
        db.session.commit()
    return render_template('contact.html')
# app.run() 
# @app.route('/post')
# def post():
#     return render_template('post.html')
 

>>>>>>> ed0efff9f63a7b6ba63ae0f9281a117607a36999
app.run(debug=True)
=======
import datetime

from flask import Flask,render_template,request
# import mysql
import mysql.connector
import mysql.connector
from datetime import datetime
# from mysql.connector import errorcode

app = Flask(__name__)

connection = mysql.connector.connect(host='localhost',
                                    database='dev',
                                    user='root',
                                    password='')
cursor = connection.cursor()

#mysql = MySQL(app)	# Init

@app.route('/')
def home():
    return render_template('index.html')
# app.run()
@app.route('/about')
def about():
    return render_template('about.html')
# app.run()
@app.route('/contact',methods=['GET','POST'])
def contact():
    if (request.method=='POST'):
    	name = request.form.get('name')
    	email = request.form.get('email')
    	phone = request.form.get('phone_num')
    	msg = request.form.get('msg')
    	cursor.execute(f"insert into contact(name, phone_num, email, msg,date) values('{name}', '{phone}', '{email}', '{msg}','{datetime.now()}')")
    	connection.commit()
    	cursor.close()
		# connection.close()
    	# return 'success'
    return render_template('contact.html')

app.run(debug=True)
>>>>>>> 11f5aed36381a603649ba767d18f43c8a2348808
