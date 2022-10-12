from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    name1 = 'Sharjeel'
    return render_template('index.html' , name2 = name1)

@app.route('/hello')
def hello():
    return 'Hello, World'
app.run()