from flask import Flask, request
from caesar import rotate_string
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

"""
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                font: 16px sans-serif;
                border-radius: 10px;
            }

            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
    """
form = """
    <form method="POST">
        <label for="rot">
        Rotate by:
        <input type="text" id="rot" name="rot" value="0"/>
        </label>
        <br><br>
        <textarea id="text" name="text"></textarea>
        <br>
        <br>
        <button type="submit">Submit Query</button>
    </form>
    """
"""
    </body>
</html>
"""

@app.route("/")
def index():
    return form
	
@app.route("/", methods=['POST'])
def encrypt():
    #do stuff with text & rot--convert data types as necessary ??
    text = request.form['text']
    rot = int(request.form['rot'])
    return '<h1>' + rotate_string(text, rot) + '</h1>'

app.run()