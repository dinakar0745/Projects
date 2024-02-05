from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def countdown():
    target_date = datetime.datetime(2024, 2, 23)

    return render_template('index.html', target_date=target_date)

if __name__ == '__main__':
    app.run(debug=True)
