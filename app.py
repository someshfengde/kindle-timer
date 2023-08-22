from flask import Flask, render_template, request
import time
import pytz
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    ist_timezone = pytz.timezone('Asia/Kolkata')    
    ist_time = datetime.now(ist_timezone).strftime('%H:%M %p %Z')
    args = request.args
    if 'land' in args: 
        return render_template('index_landscape.html', current_time = ist_time)

    return render_template('index.html', current_time = ist_time)

@app.route('/au')
def index_au():
    au_timezone = pytz.timezone('Australia/Sydney')    
    au_time = datetime.now(au_timezone).strftime('%H:%M %p %Z')
    args = request.args
    if 'land' in args: 
        return render_template('index_landscape.html', current_time = au_time)
    return render_template('index.html', current_time = au_time)

@app.route('/us')
def index_us():
    us_timezone = pytz.timezone('US/Pacific')    
    us_time = datetime.now(us_timezone).strftime('%H:%M %p %Z')
    args = request.args
    if 'land' in args: 
        return render_template('index_landscape.html', current_time = us_time)
    return render_template('index.html', current_time = us_time)

@app.route('/uk')
def index_uk():
    uk_timezone = pytz.timezone('Europe/London')    
    uk_time = datetime.now(uk_timezone).strftime('%H:%M %p %Z')
    args = request.args
    if 'land' in args: 
        return render_template('index_landscape.html', current_time = uk_time)
    return render_template('index.html', current_time = uk_time)




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port= 8000)
