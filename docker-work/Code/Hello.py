from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Flask Hello World! again'

@app.route('/Abu-Solom')
def test():
    return 'A7la messa 3lek mn gwa l python container ; Again Again !!)'

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0', port=5000)