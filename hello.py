from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello(name='Geovane'):
    return render_template('hello.html', name=name)
