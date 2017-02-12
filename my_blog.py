from flask import Flask, render_template, jsonify
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('home.html')

@app.route('/birthday')
def birthday():
    return 'December 31 1980'

@app.route('/greeting/<name>/')
def greeting(name):
    return 'Hello %s!' % name

@app.route('/sum/<int:a>/<int:b>/')
def sum(a, b):
    return '{0} + {1} = {2}'.format(a,b,a+b)

@app.route('/multiply/<int:a>/<int:b>/')
def multiply(a, b):
    return '{0} x {1} = {2}'.format(a,b,a*b)

@app.route('/subtract/<int:a>/<int:b>/')
def subtract(a, b):
    return '{0} - {1} = {2}'.format(a,b,a-b)

@app.route('/favoritefoods')
def favoritefoods():
    list = ['pizza', 'sushi', 'steak', 'tacos']
    return jsonify(list)
