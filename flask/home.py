from re import T
from flask import Flask

app=Flask(__name__)

@app.route("/")

def index():
    return "Hello World!";
@app.route("/home/<name>")
def home(name):
    return "Welcome home "+name;

if __name__ =='__main__':
    app.run(port=5000,debug=True)