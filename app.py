from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    #input_text = request.form['input_text']
    # Call the generatetext.py script with the input text
    result = subprocess.run(['python', 'calltogeneratetext.py'], capture_output=True, text=True)
    output = result.stdout
