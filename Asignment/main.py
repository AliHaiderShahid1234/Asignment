from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sign-up')
def signUp():
    return render_template('signUp.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/Trm')
def clockInAndClockOut():
    return render_template('clockin-andclockout.html')

@app.route('/help')
def helpPage():
    return render_template('help.html')

@app.route('/settings')
def helpPage():
    return render_template('settings.html')
if __name__=='__main__':
    app.run(debug=True)