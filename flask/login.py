from flask import *

app=Flask(__name__)

@app.route('/login',methods=['POST'])
def login():
    uname=request.form['uname']
    passwrd=request.form['pass']

    if uname=="ali" and passwrd=="ali":
        return "welcome %s" %uname 
    
    else :
        return "Wrong man"

if __name__ =='__main__':
    app.run(debug=True)