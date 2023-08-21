from flask import Flask, render_template
import time 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('./index.html', current_time=time.strftime('%H:%M'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8001)
