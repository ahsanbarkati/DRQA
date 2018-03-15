from flask import Flask, flash, redirect, render_template, request, url_for,jsonify
import fun
import images
app = Flask(__name__)
app.secret_key = 'some_secret'

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/ajax', methods = ['POST'])
def ajax_request():
    print("ajax called")
    username = request.form['username']
    username=images.images(username)
    return jsonify(username=username)
   

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin':
#            output="ahsan"
#            return output
            output=fun.process(request.form['username'])
            return render_template('login.html',output=output)
        
    return render_template('login.html', error=error)
if __name__ == "__main__":
    app.run()
