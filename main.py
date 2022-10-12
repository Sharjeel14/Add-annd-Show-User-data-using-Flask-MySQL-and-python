from flask import Flask, request,render_template
from flask_sqlalchemy import SQLAlchemy
import MySQLdb
from sqlalchemy import false

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/userinput'
db = SQLAlchemy(app)

class Userform(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone_number = db.Column(db.String(12), nullable=False)
    email = db.Column(db.String(25), nullable=False)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/users')
def users():
    conn = MySQLdb.connect("localhost","root","","userinput" ) 
    cursor = conn.cursor() 
    cursor.execute("select * from userform") 
    data = cursor.fetchall() #data from database 
    return render_template("users.html", value=data) 

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/addusers', methods = ['GET', 'POST'])
def addusers():
    
    if(request.method == 'POST'):
    # Add Entry to Database
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        entry = Userform(name=name, phone_number = phone, email = email )
        db.session.add(entry)
        db.session.commit()
    return render_template('addusers.html')

app.run(debug=false, host ="0.0.0.0")