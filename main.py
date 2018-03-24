from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True


form = """
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
		<!-- create your form here -->
		<form method="post">
			<label for="rot2">
			Rotate by:
			<input id="rot2" type="text" name="rot">
			</label>
			<br>
			<textarea name="text" rows="6" cols="10"></textarea>
			<br>
			<input type="submit">
		</form>
    </body>
</html>
"""

@app.route("/")
def index():
	return form

@app.route("/", methods=['POST'])	
def encrypt():
	text_e = request.form['text']
	rot_e = int(request.form['rot'])
	encrypted_string = rotate_string(text_e,rot_e)
	return '<h1>' + encrypted_string + '</h1>'
	
app.run()