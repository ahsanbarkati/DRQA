# Answer to a question on Flask mailing list
# http://librelist.com/browser//flask/2012/6/30/using-ajax-with-flask/
# NOTE: *REALLY* don't do the thing with putting the HTML in a global
#       variable like I have, I just wanted to keep everything in one
#       file for the sake of completeness of answer.
#       It's generally a very bad way to do things :)
#
from flask import (Flask, request, jsonify)
                   
app = Flask(__name__)

html_page = """<!DOCTYPE HTML>
<html>

<!DOCTYPE html>
<html lang="en" >

<head>
  <meta charset="UTF-8">
  <title>Animated Search box [Pure CSS]</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  
  <link rel='stylesheet prefetch' href='https://fonts.googleapis.com/css?family=Antic'>

      <link rel="stylesheet" href="static/style/style.css">
      <link rel="stylesheet" href="static/style/button.css">
<script>
    function myMove() {
  var elem = document.getElementById("SearchBox");   
  var pos = 220;
  var id = setInterval(frame, 1);
  function frame() {
    if (pos == 50) {
      clearInterval(id);
    } else {
      pos--; 
      elem.style.top = pos + 'px'; 
    }
  }
}
    function loadXMLDoc()
    {   
        var req = new XMLHttpRequest()
        req.onreadystatechange = function()
        {
            if (req.readyState == 4)
            {
                if (req.status != 200)
                {
                    //error handling code here
                }
                else
                {
                    var response = JSON.parse(req.responseText)
                    document.getElementById('myDiv').innerHTML = response.username
                }
            }
        }
    
        req.open('POST', '/ajax')
        req.setRequestHeader("Content-type", "application/x-www-form-urlencoded")
        var un = document.getElementById('scname').value
        var postVars = 'username='+un
        req.send(postVars)
        
        return false
    }
</script>
</head>
<body>
<br><br>
<div class="text">Wiki-Quest</div>
<form action="" method="POST">
<center><input type="text" name="scname" id="scname" class="button" placeholder="Search..." /></center>
<div id="SearchButton" onclick="return loadXMLDoc();" > <a href="#" class="btn btn-sm animated-button victoria-four">ASK ME</a>      </div>
</form>

<div id="myDiv" class="ans"></div>
</body>
</html>
"""
import fun

@app.route('/')
def index():
    return html_page
        
        
@app.route('/ajax', methods = ['POST'])
def ajax_request():
    username = int(request.form['username'])
    ans=fun.process(username)
    username=ans
    return jsonify(username=username)
    
    
if __name__ == "__main__":
    app.run(debug = True)
