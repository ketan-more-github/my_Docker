
from flask import Flask , render_template

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/')
def hello():
    return "hello , world!"

if __name__=='__main__':

    from waitress import serve
    app.run(debug= True , host='0.0.0.0')

