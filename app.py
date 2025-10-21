from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    roll = request.form['roll']
    email = request.form['email']
    year = request.form['year']
    return f"""
        <h2>Submitted Details</h2>
        <p><b>Name:</b> {name}</p>
        <p><b>Roll No:</b> {roll}</p>
        <p><b>Email:</b> {email}</p>
        <p><b>Year:</b> {year}</p>
        <br><a href="/">Go Back</a>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
