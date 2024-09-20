from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    notes = request.form['notes']
    summary = summarize_meeting_notes(notes)
    return render_template('index.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)