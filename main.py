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
                list-style-type: none;
            }
            #textarea {
                margin: 0 auto;
                width: 510px;
                height: 120px;
            }
        </style>
    </head>
    <body>
"""    
form = """
      <!-- create your form here -->
    <form action="/" method="post">
        <ul style="list-style-type:none;">
            <li>
                <label for="rot">
                    Rotate by:
                    <input type="text" id="rot" name="rot" value="0"/>
                </label>
            </li>
            <li>
                <input type="text-area" id="textarea" name="text"/>
            </li>
            <li>
                <input type="submit" value="Send"/>
            </li>
        </ul>
    </form>
"""
page_footer = """
    </body>
</html>
"""
'''@app.route("/", methods=['POST'])
def add_movie():
    new_movie = request.form['rot']

    # build response content
    new_movie_element = "<strong>" + new_movie + "</strong>"
    sentence = new_movie_element + " has been added to your Watchlist!"
    content = page_header + "<p>" + sentence + "</p>" + page_footer

    return content'''

@app.route("/", methods=['POST'])
def encrypt():
    rotation = int(request.form['rot'])
    text = request.form['text']
    sentence = "<h1>" + rotate_string(text, rotation) + "</h1>"
    content = page_header + "<p>" + sentence + "</p>" + page_footer
    return content

@app.route("/")
def index():
    content = page_header + form + page_footer
    return content

app.run()