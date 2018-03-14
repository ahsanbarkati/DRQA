from flask import Flask, flash, redirect, render_template, \
     request, url_for
import fun
app = Flask(__name__)
app.secret_key = 'some_secret'

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin':
#            output=execute('./try')
#            return output
            output=fun.process(request.form['username'])
            return render_template('index.html',output=output)
        
    return render_template('login.html', error=error)
if __name__ == "__main__":
    app.run()
