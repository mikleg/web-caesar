from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

page_header = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
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
      <!-- create your form here -->
    <form action="/" method="post">
        <label for="rot">
            Rotate by:
            <input type="text" id="rot" name="rot" value="0"/>
        </label>
        <br>
        <textarea type="text" name="text">{0}</textarea>
        <br>
        <input type="submit"/>
            
    </form>
"""
page_footer = """
    </body>
</html>
"""
@app.route("/", methods=['POST'])
def encrypt():
    rotation = int(request.form['rot'])
    text = request.form['text']
    return page_header+form.format(rotate_string(text, rotation))+page_footer

@app.route("/")
def index():
    return page_header+form.format("")+page_footer

app.run()