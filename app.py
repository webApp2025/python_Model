from flask import Flask

app = Flask(__name__)

@app.route('/in')
def index():
    return '<h1>we</h1>'

if __name__== '__main__':
    app.run(debug=True)