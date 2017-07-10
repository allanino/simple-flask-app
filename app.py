from flask import Flask

app = Flask(__name__)


@app.route('/ping')
def ping():
    return 'OK', 200


@app.route('/')
def index():
    return 'Test', 200


if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)
