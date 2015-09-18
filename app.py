
from flask import Flask, request, url_for, render_template, redirect, abort, session
import requests

app = Flask(__name__)

@app.route('/ping')
def ping():
    return 'OK', 200

@app.route('/')
def index():
    return 'Test', 200

@app.route('/docs')
def docs():
    return 'Press alt+F4 to access the true docs.', 200

if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)
